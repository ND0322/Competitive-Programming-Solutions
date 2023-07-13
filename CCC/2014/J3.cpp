#include <iostream>
using namespace std;
int main() {
  int a = 100;
  int d = 100;
  int x;
  int y;
  int n;
  cin >> n;

  for(int i = 0; i < n; i++){
    cin >> x;
    cin >> y;

    if(x > y){
      d -= x;
    
      
    }
    else if (x < y){
      a -= y;
      
    }
    
  }
  cout << a << endl;
  cout << d << endl;
  
}
