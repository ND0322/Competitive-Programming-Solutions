#include <bits/stdc++.h>

using namespace std;

typedef tuple<int,int,int> ti;
typedef pair<int,int> pi;
int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  
  int n; cin >> n;
  vector<int> program;
  program.push_back(-1);

  for(int i = 1; i <= n; i++){
    int e; cin >> e;
    program.push_back(e);
  }

  int startl,startc,endL,endc;

  cin >> startl >> startc;
  cin >> endL >> endc;



  queue<ti> q;

  vector<vector<bool>> visited(100001,vector<bool>(81,false));



  q.push(make_tuple(startl,startc,0));

  visited[startl][startc] = true;

  while(!q.empty()){
    int line,c,d;
    line = get<0>(q.front());
    c = get<1>(q.front());
    d = get<2>(q.front());

    q.pop();


    
    

    if(line == endL && c == endc){
      cout << d << "\n";
      break;
    }

    if(line == n && c == program[n]){
      ;
    }
    else if(c != program[line]){
    
      if (!visited[line][c+1]){
        q.push(make_tuple(line,c+1,d+1));
        visited[line][c+1] = true;
      }
    }
    else{

      if (!visited[line+1][1]){
        q.push(make_tuple(line+1,1,d+1));
        visited[line+1][1] = true;
      }
    }

    //left
    if(line == 1 && c == 1){
      ;
    }
    else if(c != 1){
      if (!visited[line][c-1]){
        q.push(make_tuple(line,c-1,d+1));
        visited[line][c-1] = true;
      }
    }
    else{
      if (!visited[line-1][program[line-1]]){
        q.push(make_tuple(line-1,program[line-1],d+1));
        visited[line-1][program[line-1]] = true;
      }
    }

    //down

    if(line == n){
      ;
    }
    else if(c <= program[line+1]){
      if (!visited[line+1][c]){
        q.push(make_tuple(line+1,c,d+1));

        visited[line+1][c] = true;
        
      }
    }
    else{
      if (!visited[line+1][program[line+1]]){
        q.push(make_tuple(line+1,program[line+1],d+1));
        visited[line+1][program[line+1]] = true;
        
      }
    }

    //up

    if(line == 1){
      ;
    }
    else if(c <= program[line-1]){
      if (!visited[line-1][c]){
        q.push(make_tuple(line-1,c,d+1));
        visited[line-1][c] = true;
      }
    }
    else{
      if (!visited[line-1][program[line-1]]){
        q.push(make_tuple(line-1,program[line-1],d+1));
        visited[line-1][program[line-1]] = true;
        
      }
    }
  
    
  }


  
  

  
}
