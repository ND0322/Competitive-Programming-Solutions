#include <bits/stdc++.h>

using namespace std;

const int MAXN = 205;
const int MOD = 1e9+7;

typedef pair<int,int> pii;
typedef long long ll;

int n,m, w;
ll dp[MAXN][MAXN][2];
bool in[MAXN];

vector<pii> adj[MAXN];


/*

int dfs(int node,int cap,bool type){

  cout << node << " " << cap << " " << type << endl;
  if(cap < 0) return 0;


  if(dp[node][cap][type] == -1){
    

    int ans = 0;
    if(cap == 1 && type == 1){
      dp[node][cap][type] = 1;
      return 1;
      
    }
    else if(!cap && !type){
      dp[node][cap][type] = 1;
      return 1;
    }

  
    for(pii c:adj[node]){
      
      bool ctype = c.first;
      int child = c.second;

      
      for(int i = 0; i <= cap; i++){
        if(!type){
    

          
           ans += dfs(node,cap-i,0) * (dfs(child,i,0) + dfs(child, i, 1));
          
          
        }
        else{
          if(!ctype){
            ans += dfs(node,cap-i,1) * dfs(child,i,0);
          }
          else{
            ans += dfs(node,cap-i,1) * dfs(child,i,1);
          }
        }

      }  
    }

   
  }

  return dp[node][cap][type];
}  



*/

void dfs(int node){
  dp[node][0][0] = 1;
  dp[node][1][1] = 1;



  
  for(pii c:adj[node]){
    //i hate myself
    int type = c.first;
    int child = c.second;

    
    dfs(child);

    
    for(int i = w; i >= 0; i--){

      ll were = 0;
      ll citi = 0;
      
      for(int j = 0; j <= i; j++){
        citi += dp[node][i-j][0] * ((dp[child][j][1] + dp[child][j][0]) % MOD);
        citi %= MOD;
        if(!type){
          were += dp[node][i-j][1] * dp[child][j][0];
          were %= MOD;
        }
        else{
          were += dp[node][i-j][1] * dp[child][j][1];
          were %= MOD;
        }
      }

      //cout << node << " " << i << " " << were << " " << citi << endl;

      dp[node][i][0] = citi;
      dp[node][i][1] = were;
      
    }
  }
}



int main() {
  //cyclic states annoying
  // im bald and set type as the first in the pair
  cin >> n >> w >> m;


  /*
  for(int i = 0; i <= n;i++){
    for(int j = 0; j <= w; j++){
      dp[i][j][0] = -1;
      dp[i][j][1] = -1;
    }
  }
  */

  

  while(m--){
    char type;
    int x,y;

    cin >> type >> x >> y;

    adj[x].push_back({(type == 'D' ? 1 : 0), y});
    in[y]=1;
  }

  for(int i = 1; i <= n; i++){
    if(!in[i]){
      adj[0].push_back({0,i});
    }
  }

  dfs(0);

  cout << dp[0][w][0] << '\n';

  
  

  
    
  
  
}
