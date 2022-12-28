

#include <iostream>
using namespace std;
#include <vector>
#include <queue>

using Row = vector<int>; 
using Board = vector<Row>; 


int main()
{
    int i, j; 
    cin >> i >> j; 
    Board b(i+2, Row(j+2, -1));
    char c; 
    queue<pair<int, int>> aAnalizar; // alfiles a aAnalizar
    queue<pair<int, int>> cAnalizar; // caballos a analizar
    for(int k = 1; k <= i; ++k){
        for(int l = 1; l <= j; ++l){
            cin >> c; 
            //cout << "Leo c: " << k << " " << l << endl; 
            if(c == 'K'){  // -2 represents knight
                b[k][l] = -2;
                cAnalizar.push(make_pair(k, l));
            } 
            else if(c == 'B'){ // -3 represents bishops
                b[k][l] = -3;
                aAnalizar.push(make_pair(k, l));
            } 
            else if(c == 'T') b[k][l] = -1; // traps = walls
            else if(c == '.') b[k][l] = 0; // 0 is default case
            else b[k][l] = c - '0';
            
        }
    }
    for(int i2 = 0; i2 < i+2; ++i2){
        for(int j2 = 0; j2 < j+2; ++j2){
            cout << b[i2][j2] << " "; 
        }
        cout << endl;
        
    }
    
}
