import sys

print("Number of arguments:", len(sys.argv), "arguments.")
print("Argument List:", str(sys.argv))

with open(sys.argv[-1], "r") as inputfile:
    for line in inputfile.read().split("\n"):
        if "<img" in line or "![" in line:
            print(line)
