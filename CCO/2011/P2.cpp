#include <bits/stdc++.h>

using namespace std;

typedef tuple<int,int,int> ituple;


#define INF 0x3f3f3f3f
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
 
  int s,n,e; cin >> s >> n >> e;

  vector<vector<ituple>> adj(n);

  while(e--){
    int x,y,c,type; cin >> x >> y >> c >> type;

    adj[x].push_back(make_tuple(y,c,type));
    adj[y].push_back(make_tuple(x,c,type));

    
  }
  
 
  

  priority_queue<ituple,vector<ituple>,greater<ituple>> pq;
  vector<vector<int>> distances(n,vector<int>(s + 1,INF));

  vector<bool> visited(n,false);

  pq.push(make_tuple(0,0,0));
  visited[0] = true;

  distances[0][0] = 0;

  while(!pq.empty()){
    
    int d = get<0>(pq.top());
    int node = get<1>(pq.top());
    int pS = get<2>(pq.top());

    pq.pop();
    
    

    for(ituple c:adj[node]){
      int child = get<0>(c);
      int weight = get<1>(c);
      int type = get<2>(c);


      if(type == 0){
        if(distances[child][pS] > d + weight){
          distances[child][pS] = d + weight;

          
          pq.push(make_tuple(distances[child][pS],child,pS));
           
          
          
        }
      }
      else{
        if(pS + weight <= s){
          if (distances[child][pS+weight]>d+weight){
            distances[child][pS+weight]=d+weight;

            
            pq.push(make_tuple(distances[child][pS+weight],child,pS+weight));
              
          
            
          
        }
      }
      }
      
      
    }

    
  }

  int ans = INF;

  for(int i = 0;i<=s;i++){
    if(distances[n-1][i] < ans){
      ans = distances[n-1][i];
    }
  }

  if(ans == INF){
    cout << -1 << "\n";
  }
  else{
    cout << ans << "\n";
  }
  
  
}
