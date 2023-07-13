#include <bits/stdc++.h>

using namespace std;

const int MAXN = 3e4+5;

int dp[MAXN][505], psa[MAXN], n,k,w;
int main() {
  int tt; cin >> tt;

  while(tt--){
    cin >> n >> k >> w;

    for(int i = 1; i <= n; i++){
      cin >> psa[i];
    }

    for(int i = 1; i <= n; i++){
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
        dp[i][j] = dp[i+1][j];

        dp[i][j] = max(dp[i][j], dp[min(n+1,i+w)][j-1] + psa[min(n,i+w-1)] - psa[i-1]);
      }
    }

    cout << dp[1][k] << '\n';
  }

  
}
