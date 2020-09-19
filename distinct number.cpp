#include<bits/stdc++.h>
#include<set>
using namespace std;
#define ll long long
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	ll n, t;
	cin>>n;
	set<ll> x;
	for(int i=0;i<n;i++){
		cin>>t;
		x.insert(t);
	}
	cout<<x.size();
	return 0;
	}
