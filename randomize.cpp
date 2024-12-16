//problem "randomize"
//created in 14:15:31 - Sun 01/12/2024
#include<bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
int d[N][N], l[N][N];
int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};

void dfs(int i, int j) {
    d[i][j] = 1;
    if (i == 1 && j == 1) {
        return;
    }
    int ok = 0;
    while (1) {
        vector < int > s;
        // kiểm tra xem những hướng nào có thể đi được
        for (int k = 0; k < 4; k++) {
            int u = i + dx[k];
            int v = j + dy[k];
            if (!d[u][v] && !l[u][v] && (!(i == 2 && k == 2 && d[1][1] == 0)) && (!(j == 2 && k == 1 && d[1][1] == 0))) {
                s.push_back(k);
            }
        }
        // nếu k tồn tại hướng để đi nữa thì thoát
        if (s.size() == 0) {
            break;
        }
        // random hướng có thể đi được
        int k = s[rng() % s.size()];
        int u = i + dx[k];
        int v = j + dy[k];
        if (!d[u][v] && !l[u][v]) {
            ok = 1;
            int z = (k + 1) % 4;
            l[i + dx[z]][j + dy[z]] = 1;
            z = (k + 3) % 4;
            l[i + dx[z]][j + dy[z]] = 1;
            dfs(u, v);
        }
    }
}

void solve() {
    int n;  
    cin >> n;
    for (int i = 0; i <= n + 1; i++) {
        d[0][i] = d[n + 1][i] = d[i][0] = d[i][n + 1] = 1;
    }
    dfs(n, n);
    // nếu tồn tại 2 đường đi đến được thì loại bỏ đi 1
    if (d[2][1] && d[1][2]) {
        int u = rng() % 2;
        d[1 + u][2 - u] = 0;
    }
    d[1][1] = 1;
    cout << n << "\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << d[i][j];
        }
        cout << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    #define task "task"
    freopen(task ".out", "w", stdout);
    int test = 1;
    while (test--) {
        solve();
    }
}