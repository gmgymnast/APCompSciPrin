from random import *;t=randint(0,1);g,b = [['-','-','-'],['-','-','-'],['-','-','-']],True if t==0 else False
def a(r,c,b,g):
    if b: [print('{: >2} {: >2} {: >2}'.format(*r))for r in g];r,c=int(input('Enter Row (0-2): ')),int(input('Enter Column (0-2): '));a(0,0,b,g)if r>2 or c>2 else d(g)
    if g[r][c]!='-':return a(randint(0,2),randint(0,2),b,g)if d(g)==0 else d(g)
    if g[r][c]=='-'and b:g[r][c]='O';return a(randint(0,2),randint(0,2),not b,g)if d(g)==0 else d(g)
    if (g[r][c]=='-'): g[r][c]='X';print(f'Comp Played in row {r} column {c}');return a(randint(0,2),randint(0,2),not b,g)if d(g)==0 else d(g)
def d(b):return 1 if(b[0].count('O')==3 or b[1].count('O')==3 or b[2].count('O')==3)else 2 if(b[0].count('X')==3 or b[1].count('X')==3 or b[2].count('X')==3)else e(b)
def e(b):return 1 if((b[0][0]==b[1][0]==b[2][0]=='O')or(b[0][1]==b[1][1]==b[2][1]=='O')or(b[0][2]==b[1][2]==b[2][2]=='O'))else 2 if((b[0][0]==b[1][0]==b[2][0]=='X')or(b[0][1]==b[1][1]==b[2][1]=='X')or(b[0][2]==b[1][2]==b[2][2]=='X'))else f(b)
def f(b):return(1 if b[0][0]=='O'else 2 if b[0][0]=='X'else 3 if'-'not in(b[0]+[1]+[2])else 0)if(b[0][0]==b[1][1]==b[2][2]!='-')or(b[0][2]==b[1][1]==b[2][0]!='-')else 0
print('Welcome to Tic Tac Toe!');print('Win!')if a(randint(0,2),randint(0,2),b,g)==1 else print('Lose!')if 2 else print('Draw')if 3 else print('')