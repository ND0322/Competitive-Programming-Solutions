#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

#define INF 0x3f3f3f3f


int main() {
  int n,m,a,b; cin >> n >> m >> a >> b;

  vector<vector<tuple<int,int,int>>> adj(n+1,vector<tuple<int,int,int>>());
  vector<vector<tuple<int,int,int>>> adjr(n+1,vector<tuple<int,int,int>>());

  vector<tuple<int,int,int,int>> edj;

  for(int i =0; i<m;i++){
    int x,y,l,c; cin >> x >> y >> l >> c;

    adj[x].push_back(make_tuple(y,l,c));
    adjr[y].push_back(make_tuple(x,l,c));

    edj.push_back(make_tuple(x,y,l,c));
  }

  vector<int> distances(n+1,INF);
  priority_queue<pii,vector<pii>,greater<pii>> pq;

  distances[a] = 0;
  pq.push(make_pair(0,a));

  while(!pq.empty()){
    int d = pq.top().first;
    int node = pq.top().second;

    pq.pop();

    for(tuple<int,int,int> ch:adj[node]){
      int child = get<0>(ch);
      int weight = get<1>(ch);

      if(distances[child] > d + weight){
        distances[child] = d + weight;
        pq.push(make_pair(distances[child],child));
      }
    }

    
  }

  vector<int> rdistances(n+1,INF);


  rdistances[b] = 0;
  pq.push(make_pair(0,b));

  while(!pq.empty()){
    int d = pq.top().first;
    int node = pq.top().second;

    pq.pop();

    for(tuple<int,int,int> ch:adjr[node]){
      int child = get<0>(ch);
      int weight = get<1>(ch);

      if(rdistances[child] > d + weight){
        rdistances[child] = d + weight;
        pq.push(make_pair(rdistances[child],child));
      }
    }

    
  }

  
  

  vector<pii> edges;

  for(tuple<int,int,int,int> edge:edj){
    int node = get<0>(edge);
    int child = get<1>(edge);
    int weight = get<2>(edge);
    int cost = get<3>(edge);

    int d = distances[node] + rdistances[child] + weight;

    if(d < INF){
      edges.push_back(make_pair(d,cost));
    }
    
  }

  sort(edges.begin(),edges.end());

  vector<int> costs(m,0);

  int i =0;

  for(pii edge:edges){

    
    if(!i){
      costs[i] = edge.second;
    }
    else{
      costs[i] = costs[i-1] + edge.second;
      
    }

    i++;
  }




  

  int q; cin >> q;

  while(q--){
    int d; cin >> d;
    int ans = INF;

    int l = 0;
    int r = edges.size()-1;
    

    while(l<=r){
      int mid = l + floor((r-l)/2);



      if(edges[mid].first > d){
        r = mid-1;
      }
      else{
        l = mid + 1;
      }
    }

    cout << costs[l-1] << endl;
  }
}
