import os
from pathlib import Path

print("Value of DUMMY_VAR is:", os.getenv("DUMMY_VAR"))

file = Path("data.txt")
print("Content: ", file.read_text())
