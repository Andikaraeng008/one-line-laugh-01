import os

TEXT = "My printer has never jammed on a document that didn't matter, which is how I know it can read."

assert 1 <= len(TEXT) <= 200 and TEXT.strip()

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
