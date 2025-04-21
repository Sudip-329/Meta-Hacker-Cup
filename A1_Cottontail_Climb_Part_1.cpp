#include <iostream>
#include <vector>
using namespace std;

vector<long long> generatePalindromicCandidates() {
    vector<long long> candidates;
    for (int i = 1; i <= 9; ++i) {
        for (int j = i; j <= 9; ++j) {
            long long curr = 0;
            // Build increasing part
            for (int k = i; k <= j; ++k) {
                curr = curr * 10 + k;
            }
            // Append mirrored part (excluding last digit)
            for (int k = j - 1; k >= i; --k) {
                curr = curr * 10 + k;
            }
            candidates.push_back(curr);
        }
    }
    return candidates;
}

int countValidPalindromes(long long A, long long B, long long M, const vector<long long>& candidates) {
    int count = 0;
    for (auto x : candidates) {
        if (x >= A && x <= B && x % M == 0) {
            count++;
        }
    }
    return count;
}

int main() {
    int T;
    cin >> T;
    vector<long long> palindromes = generatePalindromicCandidates();
    for (int case_num = 1; case_num <= T; ++case_num) {
        long long A, B, M;
        cin >> A >> B >> M;
        int result = countValidPalindromes(A, B, M, palindromes);
        cout << "Case #" << case_num << ": " << result << endl;
    }
    return 0;
}
