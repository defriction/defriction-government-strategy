#!/usr/bin/env python3
"""Regenera docs/ranking-contribuciones.md desde GitHub API stats/contributors."""
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

def gh_api(endpoint):
    r = subprocess.run(["gh", "api", endpoint], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None

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
            if login not in aggregated:
                aggregated[login] = {"commits": 0, "additions": 0, "deletions": 0, "repos": set()}
            weeks = entry.get("weeks", [])
            aggregated[login]["commits"] += entry.get("total", 0)
            aggregated[login]["additions"] += sum(w.get("a", 0) for w in weeks)
            aggregated[login]["deletions"] += sum(w.get("d", 0) for w in weeks)
            aggregated[login]["repos"].add(repo)

    ranking = sorted(aggregated.items(), key=lambda x: x[1]["commits"], reverse=True)

    today = date.today().isoformat()
    lines = [
        f"# Ranking de Contribuciones — defriction org\n",
        f"Actualizado automáticamente vía GitHub Action — {today}.\n",
        f"Fuente: API `stats/contributors` sobre {len(repo_ok)} repos.\n",
        "---\n",
        "## Ranking por commits\n",
        "| # | Usuario | Commits | +Líneas | -Líneas | Net | Repos |",
        "|---|--------|--------|--------|--------|-----|-------|",
    ]
    for i, (login, stats) in enumerate(ranking, 1):
        net = stats["additions"] - stats["deletions"]
        net_fmt = f"+{net}" if net >= 0 else str(net)
        lines.append(f"| {i} | {login} | {stats['commits']:,} | {stats['additions']:,} | {stats['deletions']:,} | {net_fmt} | {len(stats['repos'])} |")

    lines += ["", "## Detalle por persona"]
    for login, stats in ranking:
        lines += ["", f"### {login} — {stats['commits']} commits, +{stats['additions']:,} / -{stats['deletions']:,}, {len(stats['repos'])} repos"]
        for repo in sorted(stats["repos"]):
            lines.append(f"- {repo.split('/')[1]}")

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
