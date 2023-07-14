#include <bits/stdc++.h>


using namespace std;

const int MAXN = 1005;

string g,h;

int gs[MAXN],hs[MAXN],dp[MAXN][MAXN],n;



int main() {
  cin >> n;

  cin >> g;
  for(int i = 0; i < n; i++){
    cin >> gs[i];
  }
  cin >> h;
  for(int i = 0; i < n; i++){
    cin >> hs[i];
  }

  dp[n][n] = 0;

  for(int i = n-1; i>=0;i--){
    for(int j = n-1;j>=0;j--){
      if((g[i] == 'W' && h[j] == 'L' && gs[i] > hs[j])||(g[i] == 'L' && h[j] == 'W' && gs[i] < hs[j])){

   

        dp[i][j] = dp[i+1][j+1] + gs[i] + hs[j]; 
      }
    
      dp[i][j] = max({dp[i][j],dp[i+1][j],dp[i][j+1]});
      
    }
  }


  cout << dp[0][0] << "\n";

  
}
