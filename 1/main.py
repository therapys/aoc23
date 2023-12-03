import re

with open("input.txt", "r") as f:
    ls = f.read().split("\n")

ns = [n for l in ls for n in [re.findall(r"[0-9]", l)]]

v = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

ns = [
    n
    for l in ls
    for n in [
        re.findall(r"(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", l)
    ]
]

print(sum(int(v.get(n[0], n[0]) + v.get(n[-1], n[-1])) for n in ns))