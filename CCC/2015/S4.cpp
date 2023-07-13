#include <bits/stdc++.h>

using namespace std;

typedef tuple<int,int,int> ituple;


#define INF 0x3f3f3f3f
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int k,n,m; cin >> k >> n >> m;
  vector<vector<ituple>> adj(n + 1);

  while(m--){
    int x,y,c,h; cin >> x >> y >> c >> h;
    adj[x].push_back(make_tuple(y,c,h));
    adj[y].push_back(make_tuple(x,c,h));
  }

  int start,end; cin >> start >> end;

  priority_queue<ituple,vector<ituple>,greater<ituple>> pq;
  vector<vector<int>> distances(n+1,vector<int>(k+1,INF));

  //vector<bool> visited(n+1,false);

  pq.push(make_tuple(start,0,0));

  distances[start][0] = 0;

  while(!pq.empty()){
    int node,pDist,pHull;
    node = get<0>(pq.top());
    pDist = get<1>(pq.top());
    pHull = get<2>(pq.top());

    pq.pop();
    //visited[node] = false;

    for(ituple c:adj[node]){
      int child = get<0>(c);
      int weight = get<1>(c);
      int hull = get<2>(c);

      if(pHull + hull < k){
        if (distances[child][pHull+hull]>distances[node][pHull]+weight){
          distances[child][pHull+hull]= distances[node][pHull]+weight;

          pq.push(make_tuple(child,distances[child][pHull+hull],pHull+hull));
          //visited[child] =true;
        }
      }
      
    }

    
  }

  int ans = INF;

  for(int i = k-1;i>-1;i--){
    if(distances[end][i] < ans){
      ans = distances[end][i];
    }
  }

  if(ans == INF){
    cout << -1 << endl;
  }
  else{
    cout << ans << endl;
  }
  
  
}
