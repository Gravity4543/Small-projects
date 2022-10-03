#include<bits/stdc++.h>
#include<string>

using namespace std;
int main(){
    string yes;
do
{
    string a;
    vector<string> choose={"ROCK", "PAPER","SISSORS"};
    int computer=rand()%3;
    cout<<"choose your pick(ROCK,PAPER,SISSORS): ";
    cin>>a;
    string c=choose[computer];
    /*
    bool c=false; 
    c=find(choose.begin(),choose.end(),a)!=choose.end();
    if(c==false){cout<<"invalid!! please try again;";}*/
    cout<<"============================"<<endl;
    cout<<"Computer choose : "<<c<<endl;
    cout<<"Player choose   : "<<a<<endl;
    cout<<"============================"<<endl;
    
    if(a=="rock")
    {
        if(c=="ROCK"){cout<<"IT IS A TIE"<<endl;}
        if(c=="PAPER"){cout<<"COMPUTER WINS"<<endl;}
        if(c=="SISSORS"){cout<<"PLAYER WINS"<<endl;}
    }
    else if(a=="paper")
    {
        if(c=="PAPER"){cout<<"IT IS A TIE"<<endl;}
        if(c=="SISSORS"){cout<<"COMPUTER WINS"<<endl;}
        if(c=="ROCK"){cout<<"PLAYER WINS"<<endl;}
    }
    else if(a=="sissors")
    {
        if(c=="SISSORS"){cout<<"IT IS A TIE"<<endl;}
        if(c=="ROCK"){cout<<"COMPUTER WINS"<<endl;}
        if(c=="PAPER"){cout<<"PLAYER WINS"<<endl;}
    }

    cout<<"you wanna play again? (Y/N) : ";cin>>yes;
    cout<<endl;
}while(yes=="y");

return 0;}