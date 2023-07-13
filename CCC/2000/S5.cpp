#include <bits/stdc++.h>

using namespace std;

typedef pair<double,double> pdd;

int main() {
  //doesnt pass on dmoj, but would pass in contest
  int n; cin >> n;

  vector<pdd> ans;
  vector<bool> added(101,false);
  vector<pdd> sheep;
  while(n--){
    double x,y; cin >> x;
    cin >> y;
    sheep.push_back(make_pair(x,y));


    
  }

  

  for(double i = 0.00; i <= 1000.00; i+=0.01){

    double small = 9999999999.0;
    int ss;

    for(int s = 0; s < sheep.size();s++){
      double d = abs(sheep[s].first-i)*abs(sheep[s].first-i) + sheep[s].second * sheep[s].second;


      
      if (d <= small){
        small = d;
        ss = s;
      }
    }

    
    if (!added[ss]){
        ans.push_back(sheep[ss]);
        added[ss] = true;
    }
    
  }

  for(pdd i:ans){
    double x,y;

    x = round(i.first * 100.0)/100.0;
    y = round(i.second * 100.0)/100.0;

    cout<<"The sheep at ("<<setprecision (2) << fixed << x<<", "<< y << ") might be eaten." << endl;
  }

  
}
