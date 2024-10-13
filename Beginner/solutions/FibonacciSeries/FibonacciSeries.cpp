#include<iostream>

using namespace std;

int main()
{
	int a=0,b=1,c,n;
	cout<<"Enter The Length of fibonacci series : ";
	cin>>n;
	//0-1-1-2-3-5-----------a[n]+a[n-1]
	cout<<"output : ";
	for(int i=0;i<n;i++)
	{
		cout<<a<<" ";
		c=a+b;
		a=b;
		b=c;
	}
	return 0;	
}
