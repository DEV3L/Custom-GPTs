def escape_markdown(text: str) -> str:
    return "\n".join(map(escape_line, text.split("\n")))


def escape_line(line: str) -> str:
    if line.startswith("#"):
        return "##" + line

    if line.strip() == "---":
        return "- - -"

    return line
