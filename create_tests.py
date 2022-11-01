import sys

import os
from pathlib import Path
import math


def create_dir(path: Path):
    if not os.path.exists(path):
        os.makedirs(Path(path))
        print("Created dir", path)


def parse_clipboard() -> list[dict[str, list[str]]]:

    text = sys.stdin.readlines()
    test_cases = []
    counter = -1
    slot = None

    for element in text:
        element = element.rstrip()

        if counter == -1 and element != "inputCopy":
            print("Wrong clipboard contents!")
            exit(1)

        if element == "inputCopy":
            test_cases.append({"input": [], "output": []})
            slot = "input"
            counter += 1

        elif element == "outputCopy":
            slot = "output"

        else:
            test_cases[counter][slot].append(element)
    return test_cases


def create_test_files(test_cases, zfill):
    for i, test_case in enumerate(test_cases, 1):
        test_case_number = str(i).zfill(zfill)
        dir_name = f"test_{test_case_number}"

        create_dir(Path(dir_name))

        for key in ["input", "output"]:
            filename = Path(dir_name, f"{key}.txt")
            with open(filename, "w") as f:
                text = os.linesep.join(test_case[key])
                f.write(text)
                f.write("\n")
            print("Created file", str(filename))


if __name__ == "__main__":
    test_cases = parse_clipboard()
    zfill = int(math.log10(len(test_cases)))
    create_test_files(test_cases, zfill)
