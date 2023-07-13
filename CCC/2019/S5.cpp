#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n,k; cin >> n >> k;

  int dp[n][n];

  for(int i =0; i<n;i++){
    for(int j = 0; j < i+1;j++){
      cin >> dp[i][j];
    }
  }

  vector<int> sizes;

  sizes.push_back(k);

  int cur = k;

  while(cur > 2){
    cur = (2*cur+2)/3;
    sizes.push_back(cur);
  }
  sizes.push_back(2);
  sizes.push_back(1);

  reverse(sizes.begin(),sizes.end());

  for(int l = 1; l < (int)sizes.size() && sizes[l] <= k;l++){
    int s = sizes[l] - sizes[l-1];
    for(int i = 0; i+sizes[l]<=n;i++){
      for(int j = 0;j<=i;j++){
        dp[i][j] = max({dp[i][j],dp[i+s][j],dp[i+s][j+s]});

      }
    }
  }

  long long ans = 0;
  for(int i = 0; i+k <= n;i++){
    for(int j = 0;j<=i;j++){
      ans += dp[i][j];
    }
  }

  cout << ans << "\n";
    
}
