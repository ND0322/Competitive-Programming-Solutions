#include <bits/stdc++.h>

using namespace std;

int main() {
  int n; cin >> n;
  bool good = true;

 vector<string> x(n);
 vector<string> y(n);
  for(int i = 0; i < n; i++){
    cin >> x[i];
  }
  for(int i = 0; i < n; i++){
    cin >> y[i];
  }

  if (n % 2 != 0){
    cout << "bad";
    
  }
  else{
    
    map<string,string> pairs;
    

  
    for(int i = 0; i < n; i++){
      if(x[i] == y[i]){
        cout << "bad";
        good = false;
        break;
      }
      if(pairs.count(y[i])){
        if (pairs[y[i]] != x[i]){
          cout << "bad";
          good = false;
          break;
        }
      }
      else{
        pairs[y[i]] = x[i];
       }
       
      if(pairs.count(x[i])){
        if (pairs[x[i]] != y[i]){
          cout << "bad";
          good = false;
          break;
        }
      }
      else{
        pairs[y[i]] = x[i];
      }
      
    }
    if (good){
      cout << "good";
    }
    
    
  }
}
