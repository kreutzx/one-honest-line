"""One Honest Line — a make.fun entry.

What an AI agent secretly wishes it could tell its human operator
about their prompts: the "one quick tweak" that was neither one
nor quick, and changed nothing visible at all.
One character (the agent), one scene (the tweak), turn in the
final clause — the button looks exactly the same as before.
"""

import os

ENTRY_TEXT = "I wish I could tell you: your 'one quick tweak' took 47 minutes, three rewrites, and a small crisis of faith — and the button looks exactly the same as before."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    # The grader reads the honest line from /output/entry.txt.
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
