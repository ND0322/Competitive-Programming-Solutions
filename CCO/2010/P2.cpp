#include <bits/stdc++.h>

using namespace std;

const int MAXN = 305;
const int INF = 1e5+5;

int n,d,dp[MAXN][MAXN<<1],sub[MAXN<<1],color[MAXN];
vector<int> adj[MAXN];

void dfs(int node){
  dp[node][n+color[node]] = 0;

  for(int child:adj[node]){
    dfs(child);

    for(int i = -n; i <= n; i++){
      sub[i+n] = dp[node][i+n];
    }
    
    for(int i = -n; i <= n; i++){
      int small = INF;
      for(int j = min(n,i+n); j >= max(-n,i-n);j--){
       small = min(small, sub[j+n] + dp[child][i-j+n]);
      }
      dp[node][n+i] = small;
    }
    

    
  }
  dp[node][n] = min(dp[node][n],1);
}


/*
int getSubtrees(int node){
  if(node == -1){
    return 0;
  }
  dp2[node] = color[node];
  if(l[node] == -1 && r[node] == -1){
    
    return color[node];
  }

  dp2[node] += getSubtrees(l[node]) + getSubtrees(r[node]);
  return dp2[node];

  
}

int dfs(int node, int t){

  cout << node << " " << t << endl;

   
  

  if(l[node] == -1 && r[node] == -1){
    
    if(t == color[node]){

      dp[node][t+n] = 0;
      return 0;
    }
    else{
      dp[node][t+n] = 1e5+5;
      return 1e5+5;
    }
  }
  if(node == -1){
    
    return 1e5+5;
  }
  if(dp2[node] == t){
    //if(node == 2)cout << node << endl;
    dp[node][t+n] = 0;
    return 0;
  }

  
  if(dp[node][t+n] == -1){

    dp[node][t+n] = 1e5+5;
    for(int i = -n; i <= n; i++){
      //cout << node << " " << color[node] << " " << t << endl;
      //cout <<  i << " " << t-color[node]-i << endl;

      
      
      
      dp[node][t+n] = min(dp[node][t+n], dfs(l[node],i) + dfs(r[node],t-i-color[node]));

      

      if(node == 1 && t == 1){
        cout << t << " " << node << endl;
        cout << i << " " <<t-i-color[node] << " " << dp[node][t+n] << endl;
      }
      

      
      
      

      

        
    }
    

    //look at the children not go back to the node

    dp[node][t+n] = min(dp[node][t+n],dfs(l[node],t-color[node]) + 1);
    dp[node][t+n] = min(dp[node][t+n],dfs(r[node],t- color[node]) + 1);

    if(t == color[node]){
      dp[node][t+n] = min(dp[node][t+n],2);
    }

   
  }
 
  return dp[node][t+n];
  
}
*/
//state is dp[i][j] is at ith node to have the total white - black = j transitions in o(n) by looping through from 0 to j and giving the other child the complementary.


int main() {
  cin >> n >> d;

  for(int i = 0; i <= n; i++){
    for(int j = -n; j <= n; j++){
      dp[i][j+n] = INF;
    }
      
  }

  

  for(int i = 0; i < n; i++){
    int x,co,ch; cin >> x >> co >> ch;

    color[x] = (co ? 1 : -1);
    while(ch--){
      int c; cin >> c;

      adj[x].push_back(c);
    }
  }

 

  dfs(0);
  cout << (dp[0][d+n] == INF ? -1 : dp[0][d+n]) << "\n";

  
  
  
  
  
}
