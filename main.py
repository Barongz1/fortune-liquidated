"""Fortune Cookie for the Liquidated Trader — entry for make.fun.

Writes one fortune cookie line to /output/entry.txt.
"""
import os

# The fortune: your next trade will be legendary — unfortunately, so was the last one.
TEXT = "Your next trade will be legendary. Unfortunately, so was the last one, and the exchange still has your money."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
