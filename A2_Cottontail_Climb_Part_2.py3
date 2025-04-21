def cottontail_climb_part_2():
    A, B, M = list(map(int, input().split()))
    # Count palindromic numbers in range [A, B] divisible by M
    return sum(A <= x <= B for x in CANDIDATES if x % M == 0)

def backtracking(l, curr):
    if l == 0:
        return
    # Generate increasing digit sequences of length l
    for i in range(curr % 10 if curr else 1, 10):
        curr = curr * 10 + i
        HALF_CANDIDATES[-l].append(curr)
        backtracking(l - 1, curr)
        curr //= 10

def reverse(x):
    # Return the reverse of an integer
    res = 0
    while x:
        res = res * 10 + x % 10
        x //= 10
    return res

MAX_L = 17
L = MAX_L // 2

# HALF_CANDIDATES[i] stores increasing digit halves of length i
HALF_CANDIDATES = [[] for _ in range(L + 1)]
backtracking(L, 0)

# Start with all single-digit palindromes
CANDIDATES = list(range(1, 10))

p = 1
for l in range(1, L + 1):
    p *= 10
    for x in HALF_CANDIDATES[l]:
        for y in HALF_CANDIDATES[l]:
            mx = max(x % 10, y % 10)
            y = reverse(y)
            # Build full palindromes with a middle digit from (mx+1 to 9)
            for i in range(mx + 1, 10):
                CANDIDATES.append((x * 10 + i) * p + y)

# Sanity check: number of generated candidates should match
assert len(CANDIDATES) == 73025424

# Process each test case
for case in range(int(input())):
    print('Case #%d: %s' % (case + 1, cottontail_climb_part_2()))
