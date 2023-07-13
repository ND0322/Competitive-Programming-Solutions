#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;

int main() {
  int m,n; cin >> m >> n;

  unordered_map<int,vector<pii>> adj;

  for(int i =1;i<m+1;i++){
    for(int j = 1;j<n+1;j++){
      int e; cin >> e;
      if(adj.find(e) == adj.end()){
        adj[e] = vector<pii>();
      
        
      }

      adj[e].push_back(make_pair(i,j));
    }
  }

  queue<pii> q;
  vector<vector<bool>> visited(m+1,vector<bool>(n+1,false));

  bool check = true;

  q.push(make_pair(m,n));
  visited[m][n] = true;

  while(!q.empty()){
    pii node = q.front();
    q.pop();

    pii c = make_pair(1,1);

    if(node == c){
      cout << "yes\n";
      check = false;
      break;
      
    }

    if (adj.find(node.first * node.second) == adj.end()){
      continue;
    }

    for(pii ch:adj[node.first * node.second]){
      if(!visited[ch.first][ch.second]){
        q.push(ch);
        visited[ch.first][ch.second] = true;
      }
    }
  }

  if(check){
    cout << "no\n";
  }
}
