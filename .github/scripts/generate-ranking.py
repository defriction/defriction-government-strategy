#!/usr/bin/env python3
"""Genera docs/ranking-contribuciones.md con ranking anónimo + gráfica SVG."""
import json, subprocess, os, hashlib
from datetime import date

REPOS = [
    "defriction/defriction-landing",
    "defriction/tennis-tracker-bot-python",
    "defriction/expense-tracker-bot-python",
    "defriction/tennis-management-front-angular",
    "defriction/tennis-management-back-nestjs",
    "defriction/inventory-tracker-ia-billing-python",
    "defriction/bot-cobranzas-propiedades-horizontales",
    "defriction/financial-platform",
    "defriction/defriction-government-strategy",
]

EXCLUDE = {"claude", "astrobot-houston", "dependabot[bot]", "dependabot", "renovate[bot]"}

def gh_api(endpoint):
    r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None

def anon_id(login, seed="defriction"):
    """Deterministic short label from login hash."""
    h = hashlib.sha256(f"{seed}:{login}".encode()).hexdigest()[:8]
    return f"Colaborador {h[:4].upper()}"

def generate_bar_svg(items, title, width=600, height=None):
    """Generate a horizontal bar chart SVG. items: [(label, value, color), ...] sorted desc."""
    if not items:
        return "<!-- no data -->"

    bar_h = 32
    pad_top = 50
    pad_bot = 20
    pad_left = 150
    pad_right = 80
    label_w = pad_left - 10
    n = len(items)
    h = pad_top + n * bar_h + pad_bot
    if height and height > h:
        h = height

    max_val = max(v for _, v, _ in items)
    chart_w = width - pad_left - pad_right
    bar_colors = ["#3b82f6", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444", "#ec4899"]
    bg = "#0f172a"

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}">\n'
    svg += f'  <rect width="100%" height="100%" fill="{bg}" rx="8"/>\n'
    svg += f'  <text x="{width//2}" y="28" text-anchor="middle" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="16" font-weight="600">{title}</text>\n'

    for i, (label, val, _) in enumerate(items):
        y = pad_top + i * bar_h + bar_h // 2
        bar_w = int((val / max_val) * chart_w) if max_val > 0 else 0
        bar_w = max(bar_w, 4)
        c = bar_colors[i % len(bar_colors)]

        # label
        svg += f'  <text x="{pad_left - 8}" y="{y + 5}" text-anchor="end" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="13">{label}</text>\n'
        # bar
        svg += f'  <rect x="{pad_left}" y="{y - 10}" width="{bar_w}" height="20" rx="4" fill="{c}" opacity="0.9"/>\n'
        # value
        svg += f'  <text x="{pad_left + bar_w + 6}" y="{y + 5}" fill="{c}" font-family="system-ui,sans-serif" font-size="13" font-weight="600">{val:,}</text>\n'

    svg += '</svg>'
    return svg

def main():
    aggregated = {}
    repo_ok = []

    for repo in REPOS:
        data = gh_api(f"repos/{repo}/stats/contributors")
        if not data or not isinstance(data, list) or len(data) == 0:
            continue
        repo_ok.append(repo)
        for entry in data:
            login = entry.get("author", {}).get("login", "unknown")
            if login in EXCLUDE:
                continue
            if login not in aggregated:
                aggregated[login] = {"commits": 0, "additions": 0, "deletions": 0, "repos": set()}
            weeks = entry.get("weeks", [])
            aggregated[login]["commits"] += entry.get("total", 0)
            aggregated[login]["additions"] += sum(w.get("a", 0) for w in weeks)
            aggregated[login]["deletions"] += sum(w.get("d", 0) for w in weeks)
            aggregated[login]["repos"].add(repo)

    ranking = sorted(aggregated.items(), key=lambda x: x[1]["commits"], reverse=True)

    # Build anon mapping (stable by rank)
    anon_map = {}
    for i, (login, _) in enumerate(ranking):
        label = chr(65 + i) if i < 26 else f"{i-25:X}"
        anon_map[login] = f"Colaborador {label}"

    today = date.today().isoformat()

    # --- Build chart items ---
    chart_items = [(anon_map[login], st["commits"], None) for login, st in ranking]

    commits_svg = generate_bar_svg(chart_items, "Commits por colaborador")

    # --- Build markdown ---
    lines = [
        f"# Ranking de Contribuciones — defriction org\n",
        f"Anónimo · actualizado {today} · fuente: API `stats/contributors` sobre {len(repo_ok)} repos.\n",
        "Bots (claude, astrobot-houston, dependabot) excluidos.\n",
        "---\n",
    ]

    # SVG chart
    lines += ["## Commits por colaborador", "", f'<div align="center">', '', commits_svg, '', '</div>', '']

    # Table
    lines += ["## Tabla de contribuciones",
              "| # | Colaborador | Commits | +Líneas | -Líneas | Net | Repos |",
              "|---|-----------|--------|--------|--------|-----|-------|"]
    for i, (login, stats) in enumerate(ranking, 1):
        net = stats["additions"] - stats["deletions"]
        net_fmt = f"+{net:,}" if net >= 0 else f"{net:,}"
        lines.append(f"| {i} | {anon_map[login]} | {stats['commits']:,} | {stats['additions']:,} | {stats['deletions']:,} | {net_fmt} | {len(stats['repos'])} |")

    # Detail
    lines += ["", "## Repos alcanzados", ""]
    for repo in repo_ok:
        lines.append(f"- {repo}")

    content = "\n".join(lines) + "\n"

    out_path = "docs/ranking-contribuciones.md"
    old = ""
    try:
        with open(out_path) as f:
            old = f.read()
    except:
        pass

    if old != content:
        with open(out_path, "w") as f:
            f.write(content)
        print(f"UPDATED {out_path}")
    else:
        print("NO CHANGE")

if __name__ == "__main__":
    main()
