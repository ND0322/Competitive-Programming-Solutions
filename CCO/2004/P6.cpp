#include <bits/stdc++.h>

using namespace std;

int dp[1<<20][2];
vector<bool> mine;

int solve(int r, int cards, int p){
  if(r == 10){
    return 0;
  }
  if(dp[cards][p] == -1){
    int ans = 0;




    for(int i = 0; i < 20; i++){
      if(p == mine[i] && (cards & (1<<i))){
        int temp = cards^(1<<i);
        bool check = true;

        int opt = 9999;

        for(int j =0;j<20;j++){
          if(((!p)==mine[j])&&(temp&(1<<j))&&(floor(i/5)==floor(j/5))){
            check = false;

            if(j%5 > i%5){
              opt = min(opt,10-r-1-solve(r+1,temp^(1<<j),!p));
            }
            else{
              opt = min(opt,1+solve(r+1,temp^(1<<j),p));
            }
          }
        }

        if(check){
          for(int j =0;j<20;j++){
            if(((!p) == mine[j])&&(temp&(1<<j))){
              opt = min(opt,1+solve(r+1,temp^(1<<j),p));
            }
          }
        }


        ans = max(opt,ans);
        
      }

    
    }
    dp[cards][p] = ans;
    
  }
  return dp[cards][p];
}
int main() {
  
  
  bool check = false;

 



  while(1){

    mine = vector<bool>(20,false);
    memset(dp,-1,sizeof dp);


    for(int i = 0; i < 10; i++){
      string card;
      cin >> card;
      
      if(card.size() == 1){
        check = true;
      }
      else{

        int n = (int)(card[1])-48;


        
        if(card[0] == 'R'){

          mine[n-1] = 1;
          
        }
        else if(card[0] == 'Y'){
          mine[n+5-1] = 1;
        }
        else if(card[0] == 'G'){
          mine[n+10-1] = 1;
        }
        else if(card[0] == 'B'){
          mine[n+15-1] = 1;
        }
      }

     
     
    }

    
    if (check){
      break;
    }

    cout << solve(0,(1<<20)-1,1) << "\n";


   
   


    
  }
  
}
