#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;


typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ost;

ost t;
int rating[100000001];
int id[1000001];
int n,x,r,k,cnt;
char type;

int main() {

  
  scanf("%d",&n);

  while(n--){
    scanf(" %c",&type);

    

    if(type == 'N'){
      scan(x);
      scan(r);
      id[x] = r;
      rating[r] = x;
      t.insert(r);
      cnt++;
    }
    else if(type == 'M'){
      scan(x);
      scan(r);
      t.erase(id[x]);
      id[x] = r;
      rating[r] = x;
      t.insert(r);
    }

    else{
      scan(k);
      printf("%d\n",rating[*t.find_by_order(cnt-k)]);
      
      
    }
  }
  return 0;
}
