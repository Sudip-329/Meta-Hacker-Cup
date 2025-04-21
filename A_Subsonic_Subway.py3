def subsonic_subway():
    # Read the number of pairs N
    N = int(input())
    
    # Read N pairs of integers into a list of tuples
    pairs = [list(map(int, input().split())) for _ in range(N)]
    
    # Initialize variables to find the minimum ratio
    a, b = 0, 1
    for i, (_, x) in enumerate(pairs, 1):
        if a * x < i * b:
            a, b = i, x
    
    # Initialize variables to find the maximum ratio
    c, d = 1, 0
    for i, (x, _) in enumerate(pairs, 1):
        if c * x > i * d:
            c, d = i, x
    
    # Return the result based on the conditions
    return a / b if a * d <= c * b else -1

# Read number of test cases
T = int(input())

# Process each test case and print the result
for case_number in range(1, T + 1):
    result = subsonic_subway()
    print(f"Case #{case_number}: {result}")
