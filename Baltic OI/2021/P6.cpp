#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e5+5;
const int INF = 1e5+10;

int dp[MAXN][2][2],n;

bool state[MAXN];

vector<int> adj[MAXN];


//let dp[u][p][t] be the minimum number of moves to turn off node u and its subtree where p is true if the parent toggled their bulb and false otherwise, t is if we intend to toggle the current nod

void dfs(int node, int par){

  for(int i = 0; i <= 1; i++){
    dp[node][i][state[node] ^ i] = i;
    dp[node][i][state[node] ^ i ^ 1] = INF;
  }
  



  for(int child:adj[node]){
    if(child == par) continue;

    dfs(child,node);

    for(int i = 0; i <= 1; i++){

      int odd = dp[node][i][1];
      int even = dp[node][i][0];
      
      dp[node][i][0] = min({INF, even + dp[child][0][i], odd + dp[child][1][i]});
      dp[node][i][1] = min({INF, even + dp[child][1][i], odd + dp[child][0][i]});
      
    }
  }
}

int main() {
  cin >> n;

  for(int i = 0; i < n-1; i++){
    int x,y; cin >> x >> y;

    adj[x].push_back(y);
    adj[y].push_back(x);
  }


  for(int i = 1; i <= n; i ++){
    cin >> state[i];
  }

  dfs(1,-1);

 int ans = min(dp[1][0][0],dp[1][1][0]);

  if(ans >= INF){
    cout << "impossible\n";
  }
  else{
    cout << ans << "\n";
  }
  
}
