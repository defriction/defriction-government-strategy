#!/usr/bin/env python3
"""Genera docs/ranking-contribuciones.md — incluye Claude Code como fila IA separada."""
import json, subprocess, os, re, tempfile, shutil
from datetime import date
from collections import defaultdict

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

BOTS = {"astrobot-houston", "dependabot[bot]", "dependabot", "renovate[bot]"}
COLORS = ["#3b82f6", "#8b5cf6", "#10b981", "#f59e0b", "#ef4444", "#ec4899", "#06b6d4"]


def gh_api(endpoint):
    r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None


CLAUDE_AUTHOR_RE = re.compile(r'^claude', re.IGNORECASE)
CLAUDE_EMAILS = {"noreply@anthropic.com"}
CLAUDE_LOGINS = {"claude"}


def is_claude(author):
    """Check if an author entry is Claude Code."""
    login = author.get("login", "")
    if login.lower() in CLAUDE_LOGINS:
        return True
    return False


def bar_svg(value, max_val, color="#3b82f6", width=130, height=14):
    pct = int((value / max_val) * 100) if max_val > 0 else 0
    bar_w = max(int(pct * width / 100), 4)
    return (
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="2" width="{bar_w}" height="10" rx="3" fill="{color}" opacity="0.85"/>'
        f'</svg>'
    )


def stacked_bar_svg(direct_val, ai_val, max_val, color, width=130, height=14):
    if max_val == 0:
        return f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg"/>'
    d_w = int((direct_val / max_val) * width)
    a_w = max(0, int((ai_val / max_val) * width))
    d_w = max(d_w, 2) if direct_val > 0 else 0
    a_w = max(a_w, 2) if ai_val > 0 else 0
    return (
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        f'<rect x="0" y="2" width="{d_w}" height="10" rx="0" fill="{color}" opacity="0.85"/>'
        f'<rect x="{d_w}" y="2" width="{a_w}" height="10" rx="0" fill="{color}" opacity="0.40"/>'
        f'</svg>'
    )


def generate_bar_svg(items, title, value_key, width=650):
    bar_h = 32
    pad_top = 55
    pad_bot = 20
    pad_left = 155
    pad_right = 120
    n = len(items)
    h = pad_top + n * bar_h + pad_bot

    values = [(v["label"], v.get(value_key, 0)) for _, v in items]
    max_val = max(v for _, v in values) if values else 1
    chart_w = width - pad_left - pad_right
    bg = "#0f172a"

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}">\n'
    svg += f'  <rect width="100%" height="100%" fill="{bg}" rx="10"/>\n'
    svg += f'  <text x="{width//2}" y="26" text-anchor="middle" fill="#e2e8f0" font-family="system-ui,sans-serif" font-size="15" font-weight="700">{title}</text>\n'
    svg += f'  <text x="{width//2}" y="44" text-anchor="middle" fill="#64748b" font-family="system-ui,sans-serif" font-size="11">▮ Sólido = directos · ▯ Claro = asistidos por IA</text>\n'

    for i, (login, st) in enumerate(items):
        y = pad_top + i * bar_h + bar_h // 2
        val = st.get(value_key, 0)
        bar_w = int((val / max_val) * chart_w) if max_val > 0 else 0
        bar_w = max(bar_w, 4)
        c = COLORS[i % len(COLORS)]
        label = st["label"]
        ai_val = st.get(f"{value_key}_ai", 0)
        direct_val = val - ai_val

        svg += f'  <text x="{pad_left - 8}" y="{y + 5}" text-anchor="end" fill="#cbd5e1" font-family="system-ui,sans-serif" font-size="11">{label}</text>\n'
        d_w = int((direct_val / max_val) * chart_w) if max_val > 0 else 0
        svg += f'  <rect x="{pad_left}" y="{y - 10}" width="{max(d_w,0)}" height="20" rx="4" fill="{c}" opacity="0.85"/>\n'
        a_w = int((ai_val / max_val) * chart_w) if max_val > 0 and ai_val > 0 else 0
        if a_w > 0:
            svg += f'  <rect x="{pad_left + d_w}" y="{y - 10}" width="{a_w}" height="20" rx="4" fill="{c}" opacity="0.35"/>\n'
        svg += f'  <text x="{pad_left + bar_w + 8}" y="{y + 5}" fill="{c}" font-family="system-ui,sans-serif" font-size="12" font-weight="700">{val:,}</text>\n'

    svg += '</svg>'
    return svg


# Manual attribution of Claude Code commits (90% Santiago, 5% Julian, 5% Sneider)
CLAUDE_ATTRIBUTION = {
    "santiagorodriguezg": 0.90,   # Santiago
    "julianfrancodev":   0.05,   # Julian
    "christopher-perezm": 0.05,  # Sneider
}


def redistribute_claude(claude_stats):
    """Redistribute Claude commits/lines to humans per CLAUDE_ATTRIBUTION."""
    result = {}
    total_commits = claude_stats["commits"]
    total_adds = claude_stats["additions"]
    total_dels = claude_stats["deletions"]
    claude_repos = claude_stats["repos"]

    for login, pct in CLAUDE_ATTRIBUTION.items():
        result[login] = {
            "commits_ai": int(total_commits * pct),
            "additions_ai": int(total_adds * pct),
            "deletions_ai": int(total_dels * pct),
            "repos_ai": claude_repos,
        }

    # Assign any rounding remainder to Santiago
    assigned_commits = sum(v["commits_ai"] for v in result.values())
    assigned_adds = sum(v["additions_ai"] for v in result.values())
    assigned_dels = sum(v["deletions_ai"] for v in result.values())
    if assigned_commits < total_commits:
        result["santiagorodriguezg"]["commits_ai"] += total_commits - assigned_commits
    if assigned_adds < total_adds:
        result["santiagorodriguezg"]["additions_ai"] += total_adds - assigned_adds
    if assigned_dels < total_dels:
        result["santiagorodriguezg"]["deletions_ai"] += total_dels - assigned_dels

    return result


def main():
    aggregated = {}
    repo_ok = []
    claude_agg = {"commits": 0, "additions": 0, "deletions": 0, "repos": set()}

    # Phase 1: stats/contributors — separate human + claude data
    for repo in REPOS:
        data = gh_api(f"repos/{repo}/stats/contributors")
        if not data or not isinstance(data, list) or len(data) == 0:
            continue
        repo_ok.append(repo)
        for entry in data:
            login = entry.get("author", {}).get("login", "unknown")
            weeks = entry.get("weeks", [])
            commits = entry.get("total", 0)
            adds = sum(w.get("a", 0) for w in weeks)
            dels = sum(w.get("d", 0) for w in weeks)

            if login in BOTS:
                continue

            if is_claude(entry.get("author", {})):
                claude_agg["commits"] += commits
                claude_agg["additions"] += adds
                claude_agg["deletions"] += dels
                claude_agg["repos"].add(repo)
            else:
                if login not in aggregated:
                    aggregated[login] = {
                        "commits": 0, "commits_ai": 0,
                        "additions": 0, "additions_ai": 0,
                        "deletions": 0, "deletions_ai": 0,
                        "repos": set(), "repos_ai": set(),
                    }
                aggregated[login]["commits"] += commits
                aggregated[login]["additions"] += adds
                aggregated[login]["deletions"] += dels
                aggregated[login]["repos"].add(repo)

    # Phase 2: redistribute Claude to humans
    if claude_agg["commits"] > 0:
        claude_redist = redistribute_claude(claude_agg)
        for login, ai_st in claude_redist.items():
            if login not in aggregated:
                aggregated[login] = {
                    "commits": 0, "commits_ai": 0,
                    "additions": 0, "additions_ai": 0,
                    "deletions": 0, "deletions_ai": 0,
                    "repos": set(), "repos_ai": set(),
                }
            aggregated[login]["commits_ai"] += ai_st["commits_ai"]
            aggregated[login]["additions_ai"] += ai_st["additions_ai"]
            aggregated[login]["deletions_ai"] += ai_st["deletions_ai"]
            aggregated[login]["repos_ai"] |= ai_st["repos_ai"]

    # Build total = direct + AI
    for login, st in aggregated.items():
        st["total_commits"] = st["commits"] + st["commits_ai"]
        st["total_additions"] = st["additions"] + st["additions_ai"]
        st["total_deletions"] = st["deletions"] + st["deletions_ai"]
        st["all_repos"] = st["repos"] | st["repos_ai"]

    ranking = sorted(aggregated.items(), key=lambda x: x[1]["total_commits"], reverse=True)

    # Labels
    for i, (login, st) in enumerate(ranking):
        label = chr(65 + i) if i < 26 else f"{i-25:X}"
        st["label"] = f"Colaborador {label}"

    max_commits = max((st["total_commits"] for _, st in ranking), default=1)
    total_ai = claude_agg["commits"]
    total_human = sum(s["commits"] for _, s in ranking)
    total_all = total_human + total_ai
    pct_ai = total_ai * 100 // total_all if total_all > 0 else 0

    today = date.today().isoformat()

    # Chart items with ai breakdown
    chart_items = [(login, {
        **st,
        "commits": st["total_commits"], "commits_ai": st["commits_ai"],
        "additions": st["total_additions"], "additions_ai": st["additions_ai"],
    }) for login, st in ranking]

    commits_svg = generate_bar_svg(chart_items, "Commits totales (directos + IA)", "commits")
    adds_svg = generate_bar_svg(chart_items, "Líneas agregadas totales", "additions")

    # Markdown
    lines = [
        f"# Ranking de Contribuciones — defriction org\n",
        f"Actualizado {today} · {len(repo_ok)} repos · GitHub API `stats/contributors`\n",
        "",
        f"**Commits totales en la org:** {total_all:,} · **Directos:** {total_human:,} · **IA (Claude Code):** {total_ai:,} ({pct_ai}%)",
        "",
        f"> ℹ️ Commits de Claude Code redistribuidos con heurística: 90% Santiago, 5% Julian, 5% Sneider.",
        f"> El autor/committer real de estos commits es `Claude <noreply@anthropic.com>` — no atribuible desde git. Ajustable en `CLAUDE_ATTRIBUTION` del script.",
        "",
        "---\n",
        "## 📊 Commits\n",
        "▮ Sólido = directos · ▯ Claro = asistidos por IA (Claude Code)\n",
        f'<div align="center">\n{commits_svg}\n</div>\n',
        "## 📈 Líneas agregadas\n",
        "▮ Sólido = directos · ▯ Claro = asistidos por IA\n",
        f'<div align="center">\n{adds_svg}\n</div>\n',
        "## 📋 Tabla detallada\n",
        "| # | Colaborador | Total | Directos | IA | Barra | +Líneas | -Líneas | Net | Repos |",
        "|---|-----------|-------|----------|----|-------|--------|--------|-----|-------|",
    ]

    for i, (login, st) in enumerate(ranking, 1):
        t = st["total_commits"]
        d = st["commits"]
        ai = st["commits_ai"]
        net = st["total_additions"] - st["total_deletions"]
        net_fmt = f"+{net:,}" if net >= 0 else f"{net:,}"
        n_repos = len(st["all_repos"])
        c = COLORS[i % len(COLORS)]
        svg_bar = stacked_bar_svg(d, ai, max_commits, c)

        lines.append(
            f"| {i} | **{st['label']}** — {login} | {t:,} | {d:,} | {ai:,} | {svg_bar} | {st['total_additions']:,} | {st['total_deletions']:,} | {net_fmt} | {n_repos} |"
        )

    lines += ["", "## 🔍 Distribución por repo"]
    for login, st in ranking:
        repo_list = ", ".join(r.split("/")[1] for r in sorted(st["all_repos"]) if "/" in r)
        if st["commits_ai"] > 0:
            lines.append(f"- **{st['label']}** ({login}) — {st['total_commits']} commits ({st['commits_ai']} IA), {len(st['all_repos'])} repos: {repo_list}")
        else:
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
        print(f"\nUPDATED {out_path}")
    else:
        print("\nNO CHANGE")


if __name__ == "__main__":
    main()
