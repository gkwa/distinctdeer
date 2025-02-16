import re
from datetime import datetime


def mark_as_checked(content: str, project_name: str) -> str:
    content = content.rstrip("\n")
    lines = content.splitlines()
    pattern = rf"- \[ \].*{project_name}"

    for i, line in enumerate(lines):
        if re.search(pattern, line):
            today = datetime.now().strftime("%Y-%m-%d")
            lines[i] = f"- [x] {project_name} ✅ {today}"
            break
    else:
        raise ValueError(f"Project name '{project_name}' not found or already checked")

    return "\n".join(lines) + "\n"
