"""CrowFind: one-sentence startup pitch for make.fun's
"Ridiculous at First Glance, Real by the Second" bounty.

Writes a single pitch sentence (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, no network, no
absolute paths.
"""

import os

PITCH = (
    "CrowFind trains crows to hunt lost engagement rings in parks: "
    "heartbroken couples pay $200 per recovery, and the birds work "
    "for peanuts, literally."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
