def count_valid_palindromes():
    lower_bound, upper_bound, divisor = map(int, input().split())
    # Count palindromes within [lower_bound, upper_bound] that are divisible by 'divisor'
    return sum(lower_bound <= number <= upper_bound and number % divisor == 0 for number in PALINDROMIC_CANDIDATES)

# Precompute palindromic numbers that increase then mirror (like 12321, 45654)
PALINDROMIC_CANDIDATES = []
for start in range(1, 10):
    for end in range(start, 10):
        value = 0
        # Build increasing sequence
        for digit in range(start, end + 1):
            value = value * 10 + digit
        # Mirror the sequence (excluding the last digit to avoid duplication)
        for digit in reversed(range(start, end)):
            value = value * 10 + digit
        PALINDROMIC_CANDIDATES.append(value)

# Process multiple test cases
for test_case in range(int(input())):
    print(f"Case #{test_case + 1}: {count_valid_palindromes()}")
