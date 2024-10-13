#include<iostream>
using namespace std;

int main()
{
	string x="abbabbax";
	int len;
	string res="";
	len=x.length();
	for (int i=len-1;i>=0;i--)
	{
		res+=x[i];

	}

	if(res==x)
	{
		cout<<"Palindrome";
	}
	else
	{
		cout<<"not palindrome";
	}
	return 0;
}
