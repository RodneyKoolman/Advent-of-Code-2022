import os
import sys

elf_value = []
line_value = 0
data_file = open(os.path.join(sys.path[0], "data.txt"), "r")
lines = data_file.readlines()

for line in lines:
    line = line.strip()

    if line == "":
        elf_value.append(line_value)
        line_value = 0
    else:
        line_value += int(line)

print(f"First elf with max value: {max(elf_value)}")

line_value = 0
for _ in range(3):
    line_value += max(elf_value)
    elf_value.remove(max(elf_value))

print(f"The top 3 elfs have a total value of: {line_value}")
