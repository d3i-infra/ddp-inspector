import pathlib

datadir = pathlib.Path(__file__).parent.resolve()

file = datadir / "data" / "test.txt"

with open(file, 'r') as f:
    lines = f.readlines()

print(lines)
