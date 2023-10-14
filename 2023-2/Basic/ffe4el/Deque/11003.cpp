#include <iostream>
#include <deque>
using namespace std;

int main(){
    int n, l;
    cin >> n;
    cin >> l;

    // deque<int> dq;
    int dq[5000001];
    int a;

    for (int i =1; i<=n; i++){ //dq배열도 1부터 시작
        cin >> a;
        dq[i] = a;
    }

    int d[5000001];
    
    for(int i=1; i<=n; i++){ //d배열도 1부터 시작
        deque<int> cmp; //초기화
        if(i-n+1>0){
            for(int j=i-n+1; j<=i; j++){
                cmp.push_back(dq[j]); //cmp 덱에 넣기
            }
            for(int k=0; k<n;k++){
                cmp.p
            }
        }
        else{
            for()
        }

        d[i] = min()
    }

    return 0;
}