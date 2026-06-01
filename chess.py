board = [[2,3,4,5,6,7,8,9],
         [1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-2,-3,-4,-5,-6,-7,-8,-9]
         ]

for i in board:
    print(i)

def move(Nrow,Ncolumn,row,column):
    newpos = board[Nrow][Ncolumn]
    pos = board[row][column]
    print(str(newpos)[0])
    if newpos == 0:
        newpos = pos
        pos= 0
    
    elif str(newpos)[0] != str(pos)[0] != 0:
        newpos = pos
        pos = 0
        print("you loose")
    elif pos == -1:
        pass
    print("---------------------------------------------")
    for i in board:
        print(i)
move(4,1,6,1)
move(6,1,7,1)
move(1,1,6,1)