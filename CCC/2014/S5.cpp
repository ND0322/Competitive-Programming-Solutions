#include <bits/stdc++.h>

using namespace std;


typedef pair<int, int> pii;
typedef tuple<int,int,int> ti;




#define INF 0x3f3f3f3f


/*

int solve(int x, int last) {
  if (points[last].first * points[last].first +
          points[last].second * points[last].second ==
      1) {
    return 0;
  }

  if (dp[x][last] == -1) {
    int ans = 0;

    cur = x;
    temp = points;

    int pd = abs(temp[x].first - temp[last].first) *
                 abs(temp[x].first - temp[last].first) +
             abs(temp[x].second - temp[last].second) *
                 abs(temp[x].second - temp[last].second);

    for (int i = 0; i < points.size(); i++) {

      if (points[i].first == INF ||
          (points[i].first == 0 && points[i].second == 0)) {
        continue;
      }
      int dist = abs(points[i].first - temp[x].first) *
                     abs(points[i].first - temp[x].first) +
                 abs(points[i].second - temp[x].second) *
                     abs(points[i].second - temp[x].second);

      if (dist != 0 && dist < pd) {
        ans = max(solve(i, x) + 1, ans);
      }
    }

    dp[x][last] = ans;
  }
  return dp[x][last];
}

*/

int main() {

  
  int n;cin >> n;

  vector<pii> points;
  
  points.push_back(make_pair(0, 0));
  
  for(int i = 0; i < n; i++){
    int x, y;
    cin >> x >> y;

    points.push_back(make_pair(x, y));
  }

  

  vector<ti> all;
  vector<int> dp(n+1,0);
  vector<int> dp2(n+1,0);
  vector<int> last(n+1,0);



  
  for(int i = 0; i < n+1;i++){


    for(int j = i+1;j<n+1;j++){
      

      
      
      all.push_back(make_tuple(abs(points[i].first-points[j].first) * abs(points[i].first-points[j].first)+abs(points[i].second- points[j].second)*abs(points[i].second-points[j].second),i,j));
        
    }
  }


  

  
  


  sort(all.begin(),all.end());



  
  

  for(ti i: all){
    int dist = get<0>(i);
    int first = get<1>(i);
    int second = get<2>(i);

    if(dist != last[first]){
      last[first] = dist;
      dp2[first] = dp[first];
    }

    if(dist != last[second]){
      last[second] = dist;
      dp2[second] = dp[second];
    }

    if(first == 0){
      dp[first] = max(dp[first],dp2[second]);
    }
    else{
      dp[first] = max(dp[first],dp2[second] + 1);
      dp[second] = max(dp[second],dp2[first]+1);
    }
    
  }

  cout << dp[0] + 1 << "\n";

  
}
