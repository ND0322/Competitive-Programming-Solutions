#include <bits/stdc++.h>

using namespace std;

const int MAXN = 105;
const int INF = 2e9 + 5;
int times[MAXN], pitches[MAXN], n;


void oneD() {
  double dp[MAXN][13];

  for (int j = 1; j < 13; j++) {
      for (int i = 0; i <= n; i++) {
        dp[i][j] = -INF;
      }

      dp[0][j] = INF;
  }

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j < 13; j++) {

        if (j != pitches[i]) {
          continue;
        }

        for (int nj = 1; nj < 13; nj++) {
          
            int div = 0;
            if (nj != j) {
              div++;
            }
            
            double res =
                min(dp[i-1][nj],
                    div == 0 ? INF : ((times[i] - times[i-1]) + 0.0) / div);
            dp[i][j] = max(dp[i][j], res);
          
        }
      
    }
  }

  double ans = 0.0;

  for (int i = 1; i < 13; i++) {
    
      ans = max(ans, dp[n][i]);

  }

  if(ans == INF){
    cout << "0.00\n";
  }
  else{
    cout << setprecision(2) << fixed << ans << "\n";
  }
}

void twoD() {
  double dp[MAXN][13][13];

  for (int j = 1; j < 13; j++) {
    for (int k = j + 1; k < 13; k++) {
      for (int i = 0; i <= n; i++) {
        dp[i][j][k] = -INF;
      }

      dp[0][j][k] = INF;
    }
  }

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j < 13; j++) {
      for (int k = j + 1; k < 13; k++) {
        if (j != pitches[i] && k != pitches[i]) {
          continue;
        }

        for (int nj = 1; nj < 13; nj++) {
          for (int nk = nj + 1; nk < 13; nk++) {
            int div = 0;
            if (nj != j) {
              div++;
            }
            if (nk != k) {
              div++;
            }
            double res =
                min(dp[i-1][nj][nk],
                    div == 0 ? INF : ((times[i] - times[i-1]) + 0.0) / div);
            dp[i][j][k] = max(dp[i][j][k], res);
          }
        }
      }
    }
  }

  double ans = 0.0;

  for (int i = 1; i < 13; i++) {
    for (int j = i + 1; j < 13; j++) {
      ans = max(ans, dp[n][i][j]);
    }
  }

  if(ans == INF){
    cout << "0.00\n";
  }
  else{
    cout << setprecision(2) << fixed << ans << "\n";
  }
}

void threeD() {
  double dp[MAXN][13][13][13];

  for (int j = 1; j < 13; j++) {
    for (int k = j + 1; k < 13; k++) {
      for (int l = k + 1; l < 13; l++) {
        for (int i = 0; i <= n; i++) {
          dp[i][j][k][l] = -INF;
        }
        dp[0][j][k][l] = INF;
      }
    }
  }

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j < 13; j++) {
      for (int k = j + 1; k < 13; k++) {
        for (int l = k + 1; l < 13; l++) {
          if (j != pitches[i] && k != pitches[i] && l != pitches[i]) {
            continue;
          }

          for (int nj = 1; nj < 13; nj++) {
            for (int nk = nj + 1; nk < 13; nk++) {
              for (int nl = nk + 1; nl < 13; nl++) {
                int div = 0;
                if (nj != j) {
                  div++;
                }
                if (nk != k) {
                  div++;
                }
                if (nl != l) {
                  div++;
                }
                double res = min(
                    dp[i-1][nj][nk][nl],
                    div == 0 ? INF : ((times[i] - times[i-1]) + 0.0) / div);
                dp[i][j][k][l] = max(dp[i][j][k][l], res);
              }
            }
          }
        }
      }
    }
  }

  double ans = 0.0;

  for (int i = 1; i < 13; i++) {
    for (int j = i + 1; j < 13; j++) {
      for (int k = j + 1; k < 13; k++) {
        ans = max(ans, dp[n][i][j][k]);
      }
    }
  }

  if(ans == INF){
    cout << "0.00\n";
  }
  else{
    cout << setprecision(2) << fixed << ans << "\n";
  }
}

void fourD() {
  vector<vector<vector<vector<vector<double>>>>> dp(MAXN,vector<vector<vector<vector<double>>>>(13,vector<vector<vector<double>>>(13,vector<vector<double>>(13,vector<double>(13,0)))));





  for (int j = 1; j < 13; j++) {
    for (int k = j + 1; k < 13; k++) {
      for (int l = k + 1; l < 13; l++) {
        for (int p = l + 1; p < 13; p++) {
          

          dp[0][j][k][l][p] = INF;
        }
      }
    }
  }


  

 

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j < 13; j++) {
      for (int k = j + 1; k < 13; k++) {
        for (int l = k + 1; l < 13; l++) {
          for (int p = l + 1; p < 13; p++) {
            if (j != pitches[i] && k != pitches[i] && l != pitches[i] &&p != pitches[i]) {

              continue;
            }

            for (int nj = 1; nj < 13; nj++) {
              for (int nk = nj + 1; nk < 13; nk++) {
                for (int nl = nk + 1; nl < 13; nl++) {
                  for (int np = nl + 1; np < 13; np++) {
                    int div = 0;
                    if (nj != j) {
                      div++;
                    }
                    if (nk != k) {
                      div++;
                    }
                    if (nl != l) {
                      div++;
                    }
                    if (np != p) {
                      div++;
                    }

                    
                    double res =min(dp[i-1][nj][nk][nl][np],div == 0 ? INF: ((times[i] - times[i-1]) + 0.0) / div);

                    /*
                    if(i == 1 && j == 2 && k == 3 && l == 4 && p == 8){
                      if (res > dp[i][j][k][l][p]){
                        cout << nj << " " << nk << " " << nl << " "<< np << endl;
                        cout << res << endl;
                      }
                    }
                    */
                    
                    dp[i][j][k][l][p] =max(dp[i][j][k][l][p], res);
                    
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  

  double ans = 0.0;





  for (int i = 1; i < 13; i++) {
    for (int j = i + 1; j < 13; j++) {
      for (int k = j + 1; k < 13; k++) {
        for (int l = k + 1; l < 13; l++) {
          ans = max(ans, dp[n][i][j][k][l]);
        }
      }
    }
  }

  
  if(ans == INF){
    cout << "0.00\n";
  }
  else{
    cout << setprecision(2) << fixed << ans << "\n";
  }
  
  
}

int main() {
  int d;
  cin >> n >> d;

  for (int i = 1; i <= n; i++) {
    cin >> times[i] >> pitches[i];
  }

  

  if (d == 1) {
    oneD();
  } else if (d == 2) {
    twoD();
  } else if (d == 3) {
    threeD();
  }
  else{
    fourD();
  }
}
