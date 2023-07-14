#include <bits/stdc++.h>

using namespace std;

const int MAXN = 3e5 + 5;

typedef long long ll;

int n, m, k, colors[MAXN];
vector<int> adj[MAXN];

vector<vector<ll>> dp;
ll ans;

ll dfs(int node, int vis) {

  if(dp[node][vis] != -1){
    return dp[node][vis];
  }

  int cur = vis | (1<<colors[node]);

  dp[node][vis] = 0;
  for(int child:adj[node]){
    if(!(cur & (1<<colors[child]))){
      dp[node][vis] += dfs(child,cur) + 1;
    }
  }

  return dp[node][vis];

  

  
}

int main() {
  cin >> n >> m >> k;

  for (int i = 1; i <= n; i++) {
    cin >> colors[i];
    colors[i]--;
  }

  while (m--) {
    int x, y;
    cin >> x >> y;
    adj[x].push_back(y);
    adj[y].push_back(x);
  }

  dp = vector<vector<ll>>(n + 1, vector<ll>(32, -1));



  for (int node = 1; node <= n; node++) {
    ans += dfs(node,0);
  }

  cout << ans << "\n";
}
