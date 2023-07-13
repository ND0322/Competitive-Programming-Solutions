#include <bits/stdc++.h>

using namespace std;

int n;

typedef pair<int,int> pii;

  

void solve(int &s,int i){
  int cnt = 0;
  int left = 0;

  for(int j = i; j < n;j++){
    if(!(s & (1 << j))){
      break;
    }
    cnt++;
  }

  for(int j = i; j > -1;j--){
    if(!(s & (1 << j))){
      
      
      break;
    }
    cnt++;
    left = j;
  }

  

  cnt -= 1;



  

  if(cnt >= 4){
    s =  (s & (s + (1 << left)));
  }
  
  
  
  
}




int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> n;
  int a[26];
  string s = "";

  for(int i = 0;i<n;i++){
        cin>>a[i];
    }
  int start = 0;
  for(int i = 0;i<n;i++){
      start += a[i] << i;
  }

  
  


  queue<pii> q;

  unordered_set<int> visited;
  

  visited.insert(start);

  


  

  q.push(make_pair(start,0));

  

  while(!q.empty()){
    int node = q.front().first;
    int d = q.front().second;

 

    


    q.pop();

    if(node == 0){
      cout << d << endl;
      break;
    }

    
    for(int i = 0; i < n; i++){
      if(!(node & (1<<i))){

        
        

        

        int res = (node | (1<<i));

        
          
        solve(res,i);
  
        
  
          
  
          
  
          
      if(!visited.count(res)){
        visited.insert(res);
        q.push(make_pair(res,d+1));
        
        
      }
          
        
        

          
  
            
          }
      }
    }

  


  
  
  
  
}
