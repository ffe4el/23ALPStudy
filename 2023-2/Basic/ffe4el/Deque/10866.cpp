#include <iostream>
#include <deque>
using namespace std;

int main(){
    int n;
    cin >> n;

    deque<int> dq;

    string w;
    int a;
    int size=0;

    for(int i=0; i<n; i++){
        cin >> w;
        if(w=="push_front"){
            cin >> a;
            dq.push_front(a);
            size++;
        }
        else if(w=="push_back"){
            cin >> a;
            dq.push_back(a);
            size++;
        }
        else if(w=="pop_front"){
            if(size-1>=0){
                cout << dq.front() << endl;
                dq.pop_front();
                size--;
            }
            else{
                cout << -1 <<endl;
            }
        }
        else if(w=="pop_back"){
            if(size-1>=0){
                cout << dq.back() << endl;
                dq.pop_back();
                size--;
            }
            else{
                cout << -1 <<endl;
            }
            
        }
        else if(w=="size"){
            cout << size <<endl;
        }
        else if(w=="empty"){
            if(size==0){
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else if(w=="front"){
            if(size>0){
                cout << dq.front() << endl;
            }
            else{
                cout << -1 << endl;
            }
        }
        else if(w=="back"){
            if(size>0){
                cout << dq.back() <<endl;
            }
            else{
                cout << -1 << endl;
            }
        }
    }

    return 0;
}