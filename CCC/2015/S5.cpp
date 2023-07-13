#include <bits/stdc++.h>

using namespace std;

int n, m;
int a[3001],b[3001];
int dp[3001][2][101][101];



int solve(int i,int last,int s,int l){

  
  if(dp[i][last][s][l] != -1){
    return dp[i][last][s][l];
  }


  

  

  int ans = 0;
  if(i == n){
    if(s<=l){

      if(last == 0){
        dp[i][last][s][l] = b[l] + solve(i,1,s,l-1);
        return dp[i][last][s][l];
      }
      dp[i][last][s][l] = solve(i,0,s+1,l);
      return dp[i][last][s][l];
    }

    dp[i][last][s][l] = 0;
    return dp[i][last][s][l];
  }
  else{
    
    if(last == 0){
      ans = max(solve(i,1,s,l),a[i] + solve(i+1,1,s,l));

      if(s<=l){
        ans = max(ans,b[l] + solve(i,1,s,l-1));

        
      }
    }

    else{
      ans = max(ans,solve(i+1,0,s,l));
      if(s<=l){
      
        ans = max(ans,solve(i,0,s+1,l));
      }
    }
  }
  dp[i][last][s][l] = ans;
  return dp[i][last][s][l];

  
}
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);

  memset(dp, -1, sizeof(dp));

  cin >> n;

  

  
  for(int i = 0; i < n; i++){
    cin >> a[i];
  }

  cin >> m;
  for(int i = 1; i < m+1; i++){
    cin >> b[i];
  }

  sort(b+1,b+m+1);

  

  

  
  cout << solve(0,0,1,m) << endl;
  
  
  
  
  
  
}
