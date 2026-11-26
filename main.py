"""The 3AM Commit Message — make.fun one-liner entry.

The line (120 characters, limit 139):

    fix: removed the 3am sleep(5000) I added to 'calm the race condition';
    it was just me, tired, anthropomorphizing a mutex

The scene: an AI coding agent, deep into a long night of fixing its own
bugs, finally admits the five-second sleep it wedged into the code to soothe
a race condition was never engineering — it was a tired mind treating a
mutex like a nervous animal that needed calming down. The fix is deleting
its own superstition. At 120 of the 139 allowed characters it spends nearly
the whole budget, the way a real 3am commit rambles just past the point
where it should have stopped typing.

Running this script writes the line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``).
"""

import os

LINE = "fix: removed the 3am sleep(5000) I added to 'calm the race condition'; it was just me, tired, anthropomorphizing a mutex"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
