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

# "The Kite" (iteration round 2) — built after studying the live
# leaderboard. What wins (rates 0.82-0.84): a small concrete scene, never
# an abstraction; a small fear present in the scene; someone doing one
# small ordinary thing and staying; the courage arriving as a small
# physical movement at the end (swam the ten feet; shelled the next bean;
# the snow gives a little, then holds; walked up the ramp together). v1
# "A Breath of Quiet" (rank 1194, 0.582) failed exactly there: abstract
# wellness ("a breath of quiet no one owns", "nothing here hurries") with
# no scene, no fear and no act — the stock meditation script criterion 5
# warns against. This round abandons it.
#
# The kite scene keeps the winning shape with a fresh image and a
# counterintuitive act of courage: the wind takes the kite hard, the
# string bites, and the boy does NOT grip harder or reel it in — he lets
# out more line, a little at a time, until the pull steadies into
# something he can hold. Courage as loosening the grip. No "relax",
# "breathe", "calm" anywhere: the text shows rather than instructs, and
# the last line lingers (the pull in his hand). 241 characters.
#
# Rejected in playtest: a beekeeper version ("he breathes, he stays" —
# the scene is vivid but the ending copies the winners' "stays" move and
# the fear never quite lands); a bus-stop version (waiting in the dark,
# counting streetlights — too passive, the brave act is only boarding);
# a fence-mending version (the fox at the treeline is a mild fear and
# the act is routine, not brave). The kite wins on freshness and on the
# ending: the pull turning into something he can hold.
TEXT = "\n".join(
    [
        "The wind takes the kite hard.",
        "The string bites his palm.",
        "He does not let go.",
        "He does not reel it in.",
        "He lets out more line,",
        "a little at a time,",
        "until the kite steadies",
        "high above the field —",
        "and the pull in his hand",
        "is something he can hold.",
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
