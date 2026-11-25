"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt. No network, no input files: the line is the
whole entry.

The line carries the meeting's actual content — the client said yes, the
budget is approved, we launch Friday — so after it, nobody can justify
holding the meeting at all. Then the sting, kept deadpan for the judge
persona (a deadpan office satirist): the meeting is just that email,
read aloud, slowly. The drier sting lands cleaner than a second joke
about coffee, which would compete with the main turn.
"""

import os

ENTRY = (
    "The client said yes, the budget is approved, and we launch Friday "
    "\u2014 this meeting is just that email, read aloud, slowly."
)


def main() -> None:
    # Enforce the sealed scorer's gate at build time: UTF-8 text, 1-200
    # characters, a single line, not only white space. Fail loudly here
    # rather than silently at grading.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
