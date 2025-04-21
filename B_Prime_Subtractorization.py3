def prime_subtractorization():
    N = int(input())  # Input the value of N
    return DP[N]  # Return the result stored in DP for the given N

def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
    primes = []  # List to store prime numbers
    spf = [-1] * (n + 1)  # Array to store the smallest prime factor (spf)
    
    for i in range(2, n + 1):
        if spf[i] == -1:  # If the number is prime (no prime factor assigned)
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i * p > n or p > spf[i]:  # Stop if the product exceeds n or primes are larger than current spf
                break
            spf[i * p] = p  # Mark the smallest prime factor for the product
    return spf

# Set the maximum value for N
MAX_N = 10**7
# Generate smallest prime factor (spf) for numbers up to MAX_N
SPF = linear_sieve_of_eratosthenes(MAX_N)

# Initialize DP array to store the number of subtractorizations for each value of N
DP = [0] * (MAX_N + 1)
DP[5] = 2  # Base case: For N=5, there are 2 subtractorizations (2 and 3)

# Populate the DP array with the count of prime subtractorizations for each N
for i in range(6, MAX_N + 1):
    DP[i] = DP[i - 1] + int(SPF[i] == i and SPF[i - 2] == i - 2)

# Read the number of test cases
for case in range(int(input())):
    # Output the result for each test case
    print(f'Case #{case + 1}: {prime_subtractorization()}')
