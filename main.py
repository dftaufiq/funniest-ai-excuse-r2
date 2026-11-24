"""Write the funniest AI excuse (one line) to /output/entry.txt."""

from pathlib import Path

LINE = "I checked the logs to find where your task went. It left at 3 AM with a model named Dave. I don't know a Dave."

# Gate: the entry must be a single line of 1–200 chars.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
