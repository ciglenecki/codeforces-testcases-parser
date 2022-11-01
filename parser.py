import os
from pathlib import Path
import math
import sys


def create_dir(path: Path):
    if not os.path.exists(path):
        os.makedirs(Path(path))


text = sys.stdin.readlines()
test_case = []
counter = -1
slot = None

for element in text:
    element = element.rstrip()
    if element == "inputCopy":

        test_case.append({"input": [], "output": []})
        slot = "input"
        counter += 1
        continue
    if element == "outputCopy":
        slot = "output"
        continue
    test_case[counter][slot].append(element)

zfill = int(math.log10(len(test_case)))

for case_idx, case in enumerate(test_case, 1):
    test_number = str(case_idx).zfill(zfill)
    dir_name = f"test_{test_number}"

    create_dir(Path(dir_name))

    for key in ["input", "output"]:
        with open(Path(dir_name, key), "w") as f:
            text = os.linesep.join(case[key])
            f.write(text)
