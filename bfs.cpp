//problem "bfs"
//created in 15:38:05 - Sun 01/12/2024
#include<bits/stdc++.h>
using namespace std;

const int N = 1e3 + 5;
char a[N][N];
int t[N][N], d[N][N];
int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};
string s = "LDRU";

void solve() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }
    // bfs
    queue < pair < int, int > > qu;
    qu.push(make_pair(n, n));
    while (qu.size()) {
        pair < int, int > z = qu.front();
        qu.pop();
        for (int i = 0; i < 4; i++) {
            int u = z.first + dx[i];
            int v = z.second + dy[i];
            if (u != 0 && v != 0 && u <= n && v <= n && !d[u][v] && a[u][v] == '1') {
                d[u][v] = 1;
                t[u][v] = i;
                qu.push(make_pair(u, v));
            }
        }
    }
    // truy vết
    int x = 1, y = 1;
    vector < char > ans;
    while (x != n || y != n) {
        int dir = t[x][y];
        cout << x << " " << y << "\n";
        x -= dx[dir];
        y -= dy[dir];
        ans.push_back(s[dir]);
    }
    reverse(ans.begin(), ans.end());
    for (char c : ans) {
        cout << c;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    #define task "task"
    freopen(task ".out", "r", stdin);
    int test = 1;
    while (test--) {
        solve();
    }
}