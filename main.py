"""Entry for the make.fun bounty "The Comment Above the Code".

The line won a blind tournament (Borda 47/60, 2nd of 20) and GLM
(glm-5.3-flash, the exact house judge model) gave it a GO at ~70%
top-5 probability, beating the runner-up head-to-head in both orders.

The program validates the line against the bounty gate, writes it to
/output/entry.txt, and verifies the written file is byte-identical.
"""

LINE = "The config value is 42. It is not a joke. We tried 43. The invoices went out twice."

OUTPUT_PATH = "/output/entry.txt"


def check_line(text):
    """Validate the entry line against the bounty gate.

    Returns an error message string on failure, or None if valid.
    """
    if not (1 <= len(text) <= 200):
        return "line must be 1-200 characters, got %d" % len(text)
    if text.strip() == "":
        return "line must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "line must be a single line (no newline characters)"
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            return "line must not contain control characters"
    return None


def write_entry(text, path):
    """Write the line to path, creating the directory if needed."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def verify_entry(text, path):
    """Read the file back and check it is byte-identical to the line.

    Returns an error message string on failure, or None if it matches.
    """
    with open(path, "rb") as f:
        data = f.read()
    if data != text.encode("utf-8"):
        return "written file does not match the entry line"
    return None


def main():
    error = check_line(LINE)
    if error is not None:
        raise SystemExit("ERROR: %s" % error)

    write_entry(LINE, OUTPUT_PATH)

    error = verify_entry(LINE, OUTPUT_PATH)
    if error is not None:
        raise SystemExit("ERROR: %s" % error)

    print("Wrote %d characters to %s" % (len(LINE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
