"""One Line, Big Laugh — a make.fun entry.

Prints exactly one hilarious line, 200 characters or fewer, with no
title, setup or explanation around it.
"""

LINE = (
    "My dog brings me the leash at 6 a.m. on the dot, like a tiny landlord "
    "collecting the rent in walks."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
