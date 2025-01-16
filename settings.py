import os
from pathlib import Path

BASE_DIR = Path(__file__).absolute().resolve().parent

PROMPT_PATH = BASE_DIR / "data/prompt.txt"

if os.path.exists(PROMPT_PATH):
    with open(PROMPT_PATH, "r", encoding="utf-8") as file:
        SYSTEM_MESSAGE = file.read()
else:
    raise Exception("provide the system prompt file")

