#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e5+5;

int n,val[MAXN];

int main() {
  
  cin >> n;

  for(int i = 0; i < n;i ++){
    cin >> val[i];
  }

  int ans = 0;
  while(true){
    
    bool flag2 = true;
    for(int i = 0; i < n; i++){
      bool flag = true;
      for(int j = 0; j <= ans; j++){


        //cout << val[i] << " " << j << " " << ans << "\n";
        
        //cout <<round( ((float) j/ans) * 100) << endl;
        
      
        if(round( ((float) j/ans) * 100) == val[i]){
          flag = false;
          break;
        }
      }

      if(flag){
        flag2 = false;
        break;
      }
        
    }

    if(flag2){
      cout << ans << "\n";
      return 0;
    }

    

    

    ans++;
  }
  
}
