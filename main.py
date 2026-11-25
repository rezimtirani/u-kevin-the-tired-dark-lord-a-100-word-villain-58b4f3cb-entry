"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to
$MAKEFUN_OUTPUT_DIR/entry.txt: a fantasy villain who is secretly
just very tired, addressing the heroes who arrived at dawn. The
tiredness lives in the pauses, the deflections and the small
complaints, never in a plain statement of weariness, and the
speaker stays a villain, with a scheme and a history. Standard
library only.
"""

import os

MONOLOGUE = (
    "Heroes. Stand there while I... where was I? Ah. The prophecy. "
    "Thirty years I've kept this speech warm, and still you arrive, "
    "before the kettle, before the ravens have filed their complaints. "
    "You want the crown? Take it. It pinches. It whispers at night. "
    "My scheme \u2014 the eclipse, the army of the hollow deep, all of it "
    "\u2014 waits on one signature, and the clerk, bless his rotten heart, "
    "misplaced the quill. Again. Kneel, if you must. Monologue, then. "
    "But slowly. My knees... Look, fight me Tuesday. The doom will keep. "
    "I just need five minutes. Eyes closed. Standing."
)


def gate_check(text):
    """Check the monologue against the competition gate.

    The gate needs UTF-8 text of 1 to 600 characters, not only white
    space: one monologue of about 100 words spoken by a fantasy
    villain who is secretly just very tired. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("monologue must not be only whitespace")
    if len(cleaned) > 600:
        raise ValueError(
            "monologue is %d characters, over the 600 limit" % len(cleaned)
        )
    return cleaned


def monologue_stats(text):
    """Measure the monologue for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A monologue that drifts far from a hundred words,
    or one too short to carry a villain's history, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = gate_check(MONOLOGUE)
    stats = monologue_stats(text)
    if stats["words"] < 50:
        raise ValueError("monologue is too short to be about 100 words")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
