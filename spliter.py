#!/usr/bin/env python3
import sys

def split_file(input_path, output_prefix, num_parts=3):
    # Read all lines
    with open(input_path, 'r') as f:
        lines = f.readlines()

    total = len(lines)
    base_size = total // num_parts
    remainder = total % num_parts

    start = 0
    for i in range(num_parts):
        # give one extra line to the first 'remainder' parts
        end = start + base_size + (1 if i < remainder else 0)
        out_path = f"{output_prefix}_part{i+1}.txt"
        with open(out_path, 'w') as out:
            out.writelines(lines[start:end])
        print(f"Wrote lines {start+1}–{end} to {out_path}")
        start = end

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_text_file>")
        sys.exit(1)
    inp = sys.argv[1]
    # Use the input filename (without extension) as prefix
    prefix = inp.rsplit('.', 1)[0]
    split_file(inp, prefix)
