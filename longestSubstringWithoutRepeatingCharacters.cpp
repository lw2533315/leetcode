#include "bits/stdc++.h"

using namespace std;



int main() {
	long long a,b,n;
	cin>>n;

	for ( int i = 0; i < n; i++) {
		cin>>a;
		cin>>b;

		

		if (a == 1 && b == 1)
			cout<<"yes"<<endl;
		else {

			long long divisor = 2;
			long long small = min(a,b);
			long long big = max(a,b);
			long long divisorPow = pow(divisor, 2);
			while (divisor <= small or divisorPow <= big ) {
				if (small % divisor == 0 && big % divisorPow == 0) {
					small = small / divisor;
					big = big / divisorPow;
					a = small;
					b = big;

				} else if (small % divisorPow == 0 && big % divisor == 0 ) {
					small = small / divisorPow;
					big = big / divisor;
					a = small;
					b = big;

				} else {
					divisor ++;
				}
				divisorPow = (long long)pow(divisor, 2);
				small = min(a,b);
				big = max(a,b);




			}

			if (a == 1 && b == 1)
				cout<< "yes"<<endl;
			else
				cout<< "No"<<endl;

		}
	}
	return 0;
}