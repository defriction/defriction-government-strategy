#!/usr/bin/env python3
"""Genera docs/ranking-contribuciones.md con gráficas SVG + nombres reales."""
import json, subprocess, os
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

COLORS = ["#3b82f6", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444", "#ec4899"]


def gh_api(endpoint):
    r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None


def bar_svg(value, max_val, color="#3b82f6", width=130, height=14):
    """Mini horizontal bar SVG for table cells."""
    pct = int((value / max_val) * 100) if max_val > 0 else 0
    bar_w = max(int(pct * width / 100), 4)
    return (
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="2" width="{bar_w}" height="10" rx="3" fill="{color}" opacity="0.85"/>'
        f'</svg>'
    )


def commits_bar_svg(value, max_val, color="#3b82f6"):
    return bar_svg(value, max_val, color)


def lines_bar_svg(added, deleted, max_added, max_deleted, width=130, height=14):
    """Dual-color bar: green for additions, red for deletions."""
    total = max_added + max_deleted
    if total == 0:
        return f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg"/>'
    a_w = int((added / total) * (width * 0.55))
    d_w = int((deleted / total) * (width * 0.55))
    a_w = max(a_w, 2) if added > 0 else 0
    d_w = max(d_w, 2) if deleted > 0 else 0
    return (
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="2" width="{a_w}" height="10" rx="0" fill="#10b981" opacity="0.85"/>'
        f'<rect x="{a_w + 2}" y="2" width="{d_w}" height="10" rx="0" fill="#ef4444" opacity="0.85"/>'
        f'</svg>'
    )


def generate_bar_svg(items, title, value_key, width=600):
    """Horizontal bar chart SVG."""
    bar_h = 32
    pad_top = 50
    pad_bot = 20
    pad_left = 130
    pad_right = 100
    n = len(items)
    h = pad_top + n * bar_h + pad_bot

    values = [v[value_key] for _, v in items]
    max_val = max(values) if values else 1
    chart_w = width - pad_left - pad_right
    bg = "#0f172a"

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}">\n'
    svg += f'  <rect width="100%" height="100%" fill="{bg}" rx="10"/>\n'
    svg += f'  <text x="{width//2}" y="28" text-anchor="middle" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="16" font-weight="700">{title}</text>\n'

    for i, (login, st) in enumerate(items):
        y = pad_top + i * bar_h + bar_h // 2
        val = st[value_key]
        bar_w = int((val / max_val) * chart_w) if max_val > 0 else 0
        bar_w = max(bar_w, 4)
        c = COLORS[i % len(COLORS)]
        label = st.get("label", login)

        # label (right-aligned)
        svg += f'  <text x="{pad_left - 8}" y="{y + 5}" text-anchor="end" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="12">{label}</text>\n'
        # bar
        svg += f'  <rect x="{pad_left}" y="{y - 10}" width="{bar_w}" height="20" rx="4" fill="{c}" opacity="0.85"/>\n'
        # value
        svg += f'  <text x="{pad_left + bar_w + 8}" y="{y + 5}" fill="{c}" font-family="system-ui,sans-serif" font-size="13" font-weight="700">{val:,}</text>\n'

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

    # Anon labels
    for i, (login, st) in enumerate(ranking):
        label = chr(65 + i) if i < 26 else f"{i-25:X}"
        st["label"] = f"Colaborador {label}"

    max_commits = max((st["commits"] for _, st in ranking), default=1)
    max_adds = max((st["additions"] for _, st in ranking), default=1)
    max_dels = max((st["deletions"] for _, st in ranking), default=1)

    today = date.today().isoformat()

    # --- Chart SVGs ---
    chart_items = [(login, {**st}) for login, st in ranking]
    commits_svg = generate_bar_svg(chart_items, "Commits por colaborador", "commits")
    adds_svg = generate_bar_svg(chart_items, "Líneas agregadas", "additions")

    # --- Markdown ---
    lines = [
        f"# Ranking de Contribuciones — defriction org\n",
        f"Actualizado {today} · {len(repo_ok)} repos · API `stats/contributors`\n",
        "Bots excluidos (claude, astrobot-houston, dependabot).\n",
        "---\n",
        "## 📊 Commits\n",
        f'<div align="center">\n{commits_svg}\n</div>\n',
        "## 📈 Líneas agregadas\n",
        f'<div align="center">\n{adds_svg}\n</div>\n',
        "## 📋 Tabla detallada\n",
        "| # | Colaborador | Commits | Barra | +Líneas | -Líneas | Net | Repos |",
        "|---|-----------|--------|-------|--------|--------|-----|-------|",
    ]

    for i, (login, st) in enumerate(ranking, 1):
        net = st["additions"] - st["deletions"]
        net_fmt = f"+{net:,}" if net >= 0 else f"{net:,}"
        login_display = login
        commits_bar = commits_bar_svg(st["commits"], max_commits, COLORS[(i-1) % len(COLORS)])
        lines.append(
            f"| {i} | **{st['label']}** — {login_display} | {st['commits']:,} | {commits_bar} | {st['additions']:,} | {st['deletions']:,} | {net_fmt} | {len(st['repos'])} |"
        )

    # Detail per person
    lines += ["", "## 🔍 Distribución por repo"]
    for login, st in ranking:
        repo_list = ", ".join(r.split("/")[1] for r in sorted(st["repos"]) if "/" in r)
        lines.append(f"- **{st['label']}** ({login}) — {st['commits']} commits, {len(st['repos'])} repos: {repo_list}")

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
        print("UPDATED ranking-contribuciones.md")
    else:
        print("NO CHANGE")


if __name__ == "__main__":
    main()
