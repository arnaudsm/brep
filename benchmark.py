import os
import random

# Requires hyperfine (https://github.com/sharkdp/hyperfine)

ROWS = 100_000_000
FILE = '/tmp/test.txt'

print("Generating random list...", end="")
with open(FILE, 'w') as f:
    for _ in range(ROWS):
        f.write(f'{random.randint(0,10e10)}\t{random.randint(0,10e10)}\n')
print("✅")

print(os.path.getsize(FILE)/1e6, "MB generated")

print("Sorting...", end="")
os.system(f'sort -o "{FILE}" "{FILE}"')
print("✅")

os.system(f'hyperfine "grep ^777 {FILE}"')
os.system(f'hyperfine "brep 777 {FILE}"')

os.remove(FILE)
