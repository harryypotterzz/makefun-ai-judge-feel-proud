"""Write one warm, funny, heartfelt family scene to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
not only whitespace. The scene is two lines: a small Sunday-dinner
ritual, and the wry line that keeps a late grandmother at the table.
"""

import os

SCENE = (
    "Every Sunday, Dad sets a fourth plate for Grandma, then winks at me: "
    "\"She's just late again.\"\n"
    "Twenty years late -- and somehow dinner still tastes like she's on "
    "her way home."
)


def validate(text):
    """Mirror the sealed gate locally: 1-280 chars, non-whitespace, 1-2 lines."""
    if not text.strip():
        raise SystemExit("gate fail: entry is only whitespace")
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"gate fail: entry is {len(text)} characters, must be 1-280")
    if text.count("\n") + 1 > 2:
        raise SystemExit("gate fail: entry is more than two lines")
    text.encode("utf-8")  # gate fail if not valid UTF-8


def main():
    validate(SCENE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear the contents of the output dir, never the dir itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SCENE)
    print(f"wrote {path}: {len(SCENE)} characters")


if __name__ == "__main__":
    main()
