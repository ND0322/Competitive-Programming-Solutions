#include <bits/stdc++.h>

//todo

using namespace std;

const int MAXN = 105;
const int INF = 1e9;

int n,k[MAXN],c[MAXN];

unordered_map<int,int> dp[MAXN];

//dp state is i and abs(a-b)

int solve(int i, int dif){
  if(i == n){
    return dif;
  }

  if(dp[i].find(dif) == dp[i].end()){

    dp[i][dif] = INF;
    for(int j = 0; j <= k[i]; j++){

      

      dp[i][dif] = min(dp[i][dif],solve(i+1,abs(dif+ (c[i] * j) - ((k[i]-j) * c[i]))));
        
    }
  }

  return dp[i][dif];

  
}
int main() {
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> k[i] >> c[i];
  }

  cout << solve(0,0) << "\n";
}
