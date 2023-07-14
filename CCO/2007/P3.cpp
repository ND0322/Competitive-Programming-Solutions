#include <bits/stdc++.h>

//doesnt pass dmoj but would pass in contest

using namespace std;

const int MAXN = 1e4+105;

int n,k,w;

vector<vector<int>> dp;
vector<int> psa;
int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int tt; cin >> tt;

  while(tt--){
    cin >> n >> k >> w;

    dp = vector<vector<int>>(n+w+5,vector<int>(k+1,0));
    psa= vector<int>(n+w+5,0);

    

    for(int i = 1; i <= n; i++){
      cin >> psa[i];
    }

    for(int i = 1; i <= n+w+1; i++){
      psa[i] += psa[i-1];
    }

    //for(int i = 1; i <= n; i++){
      //cout << psa[i] << " ";
    //}
    //cout << endl;

    for(int i = n; i >= 1; i--){
      for(int j = 1; j <= k; j++){

        //cout << i << " " << j << endl;

        //cout << dp[i+1][j] << " " <<  dp[min(n+1,i+w)][j-1] + psa[min(n,i+w-1)] - psa[i-1] << endl;

        //cout << psa[min(n,i+w-1)] - psa[i-1] << endl;

        dp[i][j] = max(dp[i+1][j], dp[min(n+w+1,i+w)][j-1] + psa[min(n+w,i+w-1)] - psa[i-1]);

        //if we use two balls we can use the first ball fully, and extend the range looping through the width to choose how many pins we want

        
        

        if(j >= 2){
          for(int l = i+w+1; l <= min(n,i+2*w); l++){
            dp[i][j] = max(dp[i][j],dp[l][j-2] + psa[l-1] - psa[i-1]);
          }
        }

        

        
      }
    }

    int ans = dp[1][k];

    for(int i = 1; i <= w; i++){
      ans = max(ans,dp[i+1][k-1] + psa[i]);
    }

    cout << ans << "\n";
    
  }

  
}
