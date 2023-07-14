#include <bits/stdc++.h>

using namespace std;

const int MAXN = 205;

bool cant[MAXN][MAXN];

int n,m;


int main() {
  cin >> n >> m;

  int ans = 0;

  for(int i = 0; i < m; i++){
    int x,y; cin >> x >> y;
    cant[x][y] = true;
    cant[y][x] = true;
  }

  for(int i = 1; i <= n-2; i++){
    for(int j = i+1; j <= n-1; j++){
      for(int k = j+1; k <= n; k++){
        if(!cant[i][j] && !cant[j][k] && !cant[i][k]){
          ans++;
          
        }
      }
    }
  }

  cout << ans << "\n";
}
