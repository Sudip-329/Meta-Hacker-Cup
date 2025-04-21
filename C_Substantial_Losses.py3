MOD = 998244353

def calculate_expected_days():
    current_weight, goal_weight, max_gain_limit = map(int, input().split())
    
    # The formula calculates the expected number of days using:
    # (2 * L + 1) * (W - G) % MOD
    expected_days = (2 * max_gain_limit + 1) * (current_weight - goal_weight) % MOD
    
    return expected_days

# Read the number of test cases
T = int(input())

# Process each test case
for case_number in range(1, T + 1):
    result = calculate_expected_days()
    print(f"Case #{case_number}: {result}")
