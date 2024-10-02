#include <bits/stdc++.h>
using namespace std;

int main(){
    // Loop from 1 to 100
    for(int i=1;i<=100;i++) {
        // Check if the number is divisible by 3
        if(i%3==0 && i%5==0) cout << "FizzBuzz" << endl;
        // Check if the number is divisible by 5
        else if(i%3==0) cout << "Fizz" << endl;
        // This condition will never be true because it is already checked in the first condition
        else if(i%5==0) cout << "Buzz" << endl;
        // If none of the above conditions are true, print the number
        else cout<<i<<endl;
    }
    return 0;
}