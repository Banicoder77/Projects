#include <bits/stdc++.h>
using namespace std;

struct PairHash {
    size_t operator()(const pair<int,int>& p) const {
        return ((uint64_t)p.first << 32) ^ (uint32_t)p.second;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    cin >> h >> w;

    vector<vector<char>> l(h, vector<char>(w));
    for (int i = 0; i < h; i++)
        for (int j = 0; j < w; j++)
            cin >> l[i][j];

    int roomcount = 0;
    vector<pair<int,int>> possible = {{0,1},{1,0},{-1,0},{0,-1}};
    unordered_set<pair<int,int>, PairHash> visited;

    auto dfs = [&](pair<int,int> start) {
        vector<pair<int,int>> index;
        index.push_back(start);

        while (!index.empty()) {
            auto curr = index.back();
            index.pop_back();

            if (!visited.count(curr)) {
                visited.insert(curr);
                for (auto [dx,dy] : possible) {
                    int xn = curr.first + dx;
                    int yn = curr.second + dy;
                    if (0 <= xn && xn < h && 0 <= yn && yn < w &&
                        l[xn][yn] == '.' &&
                        !visited.count({xn,yn})) {
                        index.push_back({xn,yn});
                    }
                }
            }
        }
    };

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (l[i][j] == '.' && !visited.count({i,j})) {
                dfs({i,j});
                roomcount++;
            }
        }
    }

    cout << roomcount << '\n';
}
