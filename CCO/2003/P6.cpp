#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f

int main() {
  int t; cin >> t;
  while(t--){
    int m,n,f,k; cin >> m >> n >> f >> k;

    vector<vector<float>> gas(m+1,vector<float>(n+1,INF));

    for(int i = 0; i < k; i++){
      int x,y;
      float c; 
      cin >> x >> y >> c;

      gas[x][y] = min(gas[x][y],c);
      
    }
    
    if(f >= m+n){
        cout << "0.00" << endl;
        continue;
    }
    vector<vector<vector<float>>> costs(m+1,vector<vector<float>>(n+1,vector<float>(f+1,INF)));

    costs[1][1][f] = 0;

    
    queue<tuple<int,int,int>> q;
    q.push(make_tuple(1,1,f));

    while(!q.empty()){
      int nodex = get<0>(q.front());
      int nodey = get<1>(q.front());
      int nodef = get<2>(q.front());

      q.pop();

      

      if(nodef == 0 && gas[nodex][nodey] == INF){
        continue;
      }

      vector<pair<int,int>> next;

      if(nodex - 1 > 0){
        next.push_back(make_pair(nodex-1,nodey));
      }
      if(nodex + 1 <= m){
        next.push_back(make_pair(nodex+1,nodey));
      }
      if(nodey - 1 > 0){
        next.push_back(make_pair(nodex,nodey-1));
      }
      if(nodey + 1 <= n){
        next.push_back(make_pair(nodex,nodey+1));
      }

      for(pair<int,int> nxt:next){
        int childx = nxt.first;
        int childy = nxt.second;

        

        if(gas[nodex][nodey] != INF){
          for(int childf = 1;childf+nodef<=f;childf++){
            
            if(costs[childx][childy][nodef+childf-1] > costs[nodex][nodey][nodef] + childf * gas[nodex][nodey]){
              costs[childx][childy][nodef+childf-1] = costs[nodex][nodey][nodef] + childf * gas[nodex][nodey];
              q.push(make_tuple(childx,childy,nodef+childf-1));
            }
          }
        }
          
        
        if(nodef != 0){

  
          
          if(costs[childx][childy][nodef-1] > costs[nodex][nodey][nodef]){
            costs[childx][childy][nodef-1]=costs[nodex][nodey][nodef];
            q.push(make_tuple(childx,childy,nodef-1));
          }
        }
      }
      
      
    }

    float res = INF;

    for(float i:costs[m][n]){
      if(i < res){
        res = i;
      }
    }



    if (res < INF){
      cout << fixed<<setprecision(2)<<res<<endl;
    }
    else{
      cout << "Stranded on the shoulder" << endl;
    }

    
    
  }
}
