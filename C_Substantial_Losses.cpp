#include <iostream>
using namespace std;

const int MOD = 998244353;

long long substantial_losses(long long W, long long G, long long L) {
    long long diff = W - G;
    long long factor = 2 * L + 1;
    return (factor % MOD) * (diff % MOD) % MOD;
}

int main() {
    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        long long W, G, L;
        cin >> W >> G >> L;
        long long result = substantial_losses(W, G, L);
        cout << "Case #" << case_num << ": " << result << "\n";
    }
    return 0;
}
