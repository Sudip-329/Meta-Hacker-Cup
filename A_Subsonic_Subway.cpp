#include <iostream>
#include <vector>
using namespace std;

double subsonic_subway() {
    int N;
    cin >> N;
    vector<pair<int, int>> A_B(N);

    for (int i = 0; i < N; ++i) {
        cin >> A_B[i].first >> A_B[i].second;
    }

    int a = 0, b = 1;
    for (int i = 0; i < N; ++i) {
        int x = A_B[i].second;
        if (1LL * a * x < 1LL * (i + 1) * b) {
            a = i + 1;
            b = x;
        }
    }

    int c = 1, d = 0;
    for (int i = 0; i < N; ++i) {
        int x = A_B[i].first;
        if (1LL * c * x > 1LL * (i + 1) * d) {
            c = i + 1;
            d = x;
        }
    }

    if (1LL * a * d <= 1LL * c * b) {
        return (double)a / b;
    } else {
        return -1;
    }
}

int main() {
    int T;
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        double result = subsonic_subway();
        cout << "Case #" << case_num << ": ";
        if (result == -1)
            cout << -1 << endl;
        else
            cout<< result <<endl;
    }
    return 0;
}
