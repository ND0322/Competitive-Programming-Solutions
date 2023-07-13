#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f
typedef pair<int,int> pii;

int main() {
  
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int n,w,d; cin >> n >> w >> d;

  vector<vector<int>> adj(n+1,vector<int>());

  for(int i = 0; i < w; i ++){
    int x,y; cin >> x >> y;

    adj[y].push_back(x);
  }

  queue<int> q;
  vector<bool> visited(n+1,false);
  vector<int> distances(n+1,INF);

  q.push(n);
  visited[n] = true;
  distances[n] = 0;

  while(!q.empty()){
    int node = q.front();
    q.pop();

    for(int child:adj[node]){
      if(!visited[child]){
        q.push(child);
        visited[child] = true;
        distances[child] = distances[node] + 1;
      }
    }
  }

  vector<int> subway(n,-1);

  for(int i = 0; i < n; i++){
    cin >> subway[i];
  }

  multiset<pii> times;

  for(int i = 0; i < n; i++){times.insert(make_pair(i+distances[subway[i]],subway[i]));}

  for(int i = 0; i < d; i++){
    int x,y; cin >> x >> y;

    times.erase(make_pair(distances[subway[x-1]]+x-1,subway[x-1]));

    

    times.insert(make_pair(y-1+distances[subway[x-1]],subway[x-1]));

    times.erase(make_pair(distances[subway[y-1]]+y-1,subway[y-1]));
    

    times.insert(make_pair(x-1+distances[subway[y-1]],subway[y-1]));

    pii ans = *times.begin();

    cout << ans.first << "\n";

    int temp = subway[x-1];
    subway[x-1] = subway[y-1];
    subway[y-1] = temp;

    

    
    

  }
  
}
