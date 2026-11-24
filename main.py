#!/usr/bin/env python3
"""CrowFind - make.fun entry.

Writes one original pitch line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure stdlib, no network, no secrets, no hard-coded output path.
"""

import os

# The joke: ridiculous at first glance (trained crows), real by the
# second ($200 per recovery is a credible price) — and the birds work
# for peanuts, literally.
PITCH = (
    "CrowFind trains crows to hunt lost engagement rings in parks: "
    "heartbroken couples pay $200 per recovery, and the birds work "
    "for peanuts, literally."
)


def main() -> int:
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), (
        "pitch must be exactly one sentence"
    )
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
