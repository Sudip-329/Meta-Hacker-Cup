#include <iostream>
#include <vector>
using namespace std;

const int MAX_N = 10000000;
vector<int> SPF(MAX_N + 1, -1); 
vector<int> DP(MAX_N + 1, 0);

void linear_sieve_of_eratosthenes() {
    vector<int> primes;
    for (int i = 2; i <= MAX_N; ++i) {
        if (SPF[i] == -1) {
            SPF[i] = i;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (i * p > MAX_N || p > SPF[i])
                break;
            SPF[i * p] = p;
        }
    }
}

void preprocess_dp() {
    DP[5] = 2;
    for (int i = 6; i <= MAX_N; ++i) {
        DP[i] = DP[i - 1];
        if (SPF[i] == i && SPF[i - 2] == i - 2) { 
            DP[i]++;
        }
    }
}

int prime_subtractorization(int N) {
    return DP[N];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    linear_sieve_of_eratosthenes();
    preprocess_dp();

    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        int N;
        cin >> N;
        cout << "Case #" << case_num << ": " << prime_subtractorization(N) << '\n';
    }

    return 0;
}
