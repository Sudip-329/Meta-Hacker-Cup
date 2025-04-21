#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int count=1;
    while(t--)
    {
        int s,d,k;
        cin>>s>>d>>k;
        int buns = 0;
        buns = s*2 + d*2;
        int patty = 0;
        patty = s + d*2;
        cout<<"Case #"<<count<<": ";
        if(buns>=(k+1))
        {
            if(patty >= k)
            {
                cout<<"YES"<<endl;
            }
            else{
                cout<<"NO"<<endl;
            }
        }
        else{
            cout<<"NO"<<endl;
        }
        count++;
    }
}