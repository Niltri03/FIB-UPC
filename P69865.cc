



#include <iostream>
using namespace std;
#include <vector>
#include <queue>

using Row = vector<int>; 
using Board = vector<Row>; 


void analizaAlfil(int x, int y, Board &b, int &monedas){
    if(b[x][y] == -1); 
    else {
        if(b[x][y] > 0){
            monedas+=b[x][y];
            b[x][y] = 0; 
        }
        b[x][y] = -1; 
        analizaAlfil(x+1, y+1, b, monedas);
        analizaAlfil(x+1, y-1, b, monedas);
        analizaAlfil(x-1, y+1, b, monedas);
        analizaAlfil(x-1, y-1, b, monedas);
        b[x][y] = -2; 
        
    }
    
    
}

void analizaCaballo(int x, int y, int maxx, int maxy, Board &b, int &monedas){
    if (x < 0) or (y < 0) or (y > maxy ) or (x > maxx);
    else if(b[x][y] == -1);
    else { 
        if(b[x][y] > 0){
            monedas+=b[x][y];
            b[x][y] = 0; 
        }
        b[x][y] = -1; 
        analizaCaballo(x+2, y+1, b, monedas);
        analizaCaballo(x+2, y-1, b, monedas);
        analizaCaballo(x+1, y+2, b, monedas);
        analizaCaballo(x+1, y-2, b, monedas);
        analizaCaballo(x-2, y+1, b, monedas);
        analizaCaballo(x-2, y-1, b, monedas);
        analizaCaballo(x-1, y+2, b, monedas);
        analizaCaballo(x-1, y-2, b, monedas);
        b[x][y] = -2; 
        
    }
    
    
}
    
    
}

int main()
{
    int i, j; 
    cin >> i >> j; 
    char c; 
    Board b(i+2, Row(j+2, -1));
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
    int monedas = 0; 
    while(not cAnalizar.empty()){
        pair<int, int> act = cAnalizar.top(); 
        analizaCaballo(act.first, act.second, i+2, j+2, b, monedas); 
        cAnalizar.pop(); 
        
    }
    while(not aAnalizar.empty()){
        pair<int, int> act = aAnalizar.top(); 
        analizaAlfil(act.first, act.second, b, monedas); 
        aAnalizar.pop(); 
        
    }
}
