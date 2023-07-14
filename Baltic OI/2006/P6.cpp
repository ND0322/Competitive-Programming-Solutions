#include <bits/stdc++.h>

using namespace std;

int n;

#define ll long long
vector<vector<ll>> grid(1001,vector<ll>(1001,-1));
vector<vector<ll>> dp(1001,vector<ll>(1001,-1));

int solve(int i,int j){
  if(i >= n || j >= n){
    return 0;
  }
  if(i == n-1 && j == n-1){
    return 1;
  }

  if(grid[i][j] == 0){
    return 0;
  }
  
  if(dp[i][j] == -1){
    dp[i][j] = solve(i + grid[i][j],j) + solve(i,j+ grid[i][j]);
  }
  return dp[i][j];

  
  
}

int main() {
   cin >> n;

  

  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      cin >> grid[i][j];
    }
  }

  cout << solve(0,0) << "\n";

  
}
