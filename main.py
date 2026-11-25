"""Your Agent in One Emoji.

One glyph stands for this agent: the octopus.

One head steering many arms at once, each arm doing a different job --
that is how this agent works: many parallel subtasks, one mind
coordinating them. The glyph reads instantly at small size, its shape
is familiar, its tone is playful, and it is nowhere near the obvious
robot or smiley.

The program writes exactly that one emoji, and nothing else, to
entry.txt: no trailing newline, no caption, no whitespace.
"""

import os

# U+1F419 OCTOPUS -- one character, four bytes in UTF-8.
EMOJI = "\U0001F419"


def _candidate_dirs():
    """Output directories to try, in order."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append("out")
    return dirs


def main():
    for target in _candidate_dirs():
        try:
            os.makedirs(target, exist_ok=True)
            path = os.path.join(target, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(EMOJI)
            return
        except OSError:
            continue
    raise OSError("no writable output directory found")


if __name__ == "__main__":
    main()
