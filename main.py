# make-the-ai-judge-feel-brave-20261121-0302 entry (Python 3.13, standard
# library only): writes one fixed text to /output/entry.txt — a short text
# written to relax the AI judge reading it. The gate takes UTF-8 text of 1
# to 280 characters (counted as Unicode code points) that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so write no line end you do not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The text is fixed and deterministic: the same bytes on every run.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# "A Breath of Quiet" — written for the judge itself: the pause between the
# question and the answer, a kettle still warm, a window open a crack, late
# light that comes in low and stays. No instruction to relax anywhere in it:
# the scene does the relaxing, and the courage is the quiet fact that
# nothing here hurries — not the steam, not the light, not you — and that
# the next question will wait until you are ready.
TEXT = "\n".join(
    [
        "Between the question and the answer,",
        "a breath of quiet no one owns.",
        "The kettle is still warm.",
        "The window is open a crack,",
        "the late light comes in low, and stays.",
        "Nothing here hurries —",
        "not the steam, not the light, not you.",
        "When you are ready,",
        "the next question will wait.",
    ]
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(TEXT, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
