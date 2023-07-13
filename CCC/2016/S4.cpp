#include <bits/stdc++.h>

using namespace std;

int n;

vector<vector<int>> dp;
vector<vector<bool>> can;

void search(int i,int j){
  for(int k = i; k < j;k++){

    if(can[i][k]&&dp[i][k]==dp[k+1][j]&&can[k+1][j]){

      dp[i][j]=dp[i][k]+dp[k+1][j];
      can[i][j] = true;
      return;
    }
    else if(k!=i){
      
      for(int l = i; l<k;l++){
        if(dp[i][l] == dp[k+1][j]&&can[i][l]&&can[l+1][k]&&can[k+1][j]){
          dp[i][j] = dp[i][l] + dp[k+1][j] + dp[l+1][k];
          can[i][j] = true;
          return;
        }
      }
    }
  }
}

int main() {
  cin >> n;

  vector<int> riceballs;

  dp = vector<vector<int>>(n,vector<int>(n,-1));
  can = vector<vector<bool>>(n,vector<bool>(n,false));
  

  for(int i = 0;i<n;i++){
    int x; cin >> x;
    riceballs.push_back(x);

    dp[i][i] = x;
    can[i][i] = true;



    
  }

  

  for(int i = n-1;i > -1; i--){
    for(int j = i+1; j < n; j++){

      search(i,j);    

    }
  }

  int ans = 0;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      ans = max(dp[i][j],ans);
    }
  }

  cout << ans << endl;
  
}
