def create_board():
    board = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
    value = [0,2,2,2,2,2,2,2,2,2]
    return board, value

def DrawBoard(board):    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")  

def position(value,a,b,c):
    if value[a] == 2:
        return a
    elif value[b] == 2:
        return b
    elif value[c] == 2:
        return c
    return 0

def posswin(board, value, player):
    if player == 1:
        req_prod = 50
        
        #HORIZONTAL CHECK
        
        if value[1]*value[2]*value[3] == req_prod:
            return position(value,1,2,3)
        elif value[4]*value[5]*value[6] == req_prod:
            return position(value,4,5,6)
        elif value[7]*value[8]*value[9] == req_prod:
            return position(value,7,8,9)
        
        #VERTICAL CHECK
        
        if value[1]*value[4]*value[7] == req_prod:
            return position(value,1,4,7)
        elif value[2]*value[5]*value[8] == req_prod:
            return position(value,2,5,8)
        elif value[3]*value[6]*value[9] == req_prod:
            return position(value,3,6,9)
        
        #DIAGNOL CHECK
        
        if value[1]*value[5]*value[9] == req_prod:
            return position(value,1,5,9)
        elif value[3]*value[5]*value[7] == req_prod:
            return position(value,3,5,7)
        
        return 0
    else:
        req_prod = 18
        
        #HORIZONTAL CHECK
        
        if value[1]*value[2]*value[3] == req_prod:
            return position(value,1,2,3)
        elif value[4]*value[5]*value[6] == req_prod:
            return position(value,4,5,6)
        elif value[7]*value[8]*value[9] == req_prod:
            return position(value,7,8,9)
        
        #VERTICAL CHECK
        
        if value[1]*value[4]*value[7] == req_prod:
            return position(value,1,4,7)
        elif value[2]*value[5]*value[8] == req_prod:
            return position(value,2,5,8)
        elif value[3]*value[6]*value[9] == req_prod:
            return position(value,3,6,9)
        
        #DIAGNOL CHECK
        
        if value[1]*value[5]*value[9] == req_prod:
            return position(value,1,5,9)
        elif value[3]*value[5]*value[7] == req_prod:
            return position(value,3,5,7)
        
        return 0
        
def GoMake2(board,value,Mark):
    if board[5] == ' ':
        return 5
    else:
        list = [2,4,6,8]
        for i in list:
            if board[i] == ' ':
                return i

def GO(board, value,turn,player = 1):
    if player == 1:
        Mark = 'X'
        if turn == 1:
            board[1] = Mark
            value[1] = 5
       
        elif turn == 3:
            if board[9] == ' ':
                board[9] = Mark
                value[9] = 5
            else:
                board[3] = Mark
                value[3] = 5
                
        elif turn == 5:
            pos = posswin(board, value, player)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 5
                return 1
            pos = posswin(board, value, 2)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 5
            elif board[7] == ' ':
                board[7] = Mark
                value = 5
            else:
                board[3] = Mark
                value[3] = 5
                
        elif turn == 7 or turn == 9:
            pos = posswin(board, value, player)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 5
                return 1
            pos = posswin(board, value, 2)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 5
            else:
                for i in board:
                    if board[int(i)] == ' ':
                        board[int(i)] = Mark
                        value = 5
                        
    if player == 2:
        Mark = 'O'
        if turn == 2:
            if board[5] == ' ':
                board[5] = Mark
                value[5] = 3
            else:
                board[1] = Mark
                value[1] = 3
        elif turn == 4:
            pos = posswin(board, value, 1)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 3
            else:
                x = GoMake2(board,value,Mark)
                board[x] = Mark
                value[x] = 3
        elif turn == 6:
            pos = posswin(board, value, player)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 3
                return 1
            pos = posswin(board, value, player)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 3
            else:
                x = GoMake2(board,value,Mark)
                board[x] = Mark
                value[x] = 3
        elif turn == 8:
            pos = posswin(board, value, player)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 3
                return 1
            pos = posswin(board, value, 1)
            if pos != 0:
                board[pos] = Mark
                value[pos] = 3
            else:
                for i in board:
                    if board[int(i)] == ' ':
                        board[int(i)] = Mark
                        value = 3
    return 0

def player_input(board):
    pos = int(input('enter the position u wanna place X :  '))
    if board[pos] != ' ':
        print('The position is already occupied....Try another')
        pos = player_input(board)
    return pos

def player_win(value,player):
    if player == 1:
        req_prod = 125
        
        #HORIZONTAL CHECK
        
        if value[1]*value[2]*value[3] == req_prod:
            return 2
        elif value[4]*value[5]*value[6] == req_prod:
            return 2
        elif value[7]*value[8]*value[9] == req_prod:
            return 2
        
        #VERTICAL CHECK
        
        if value[1]*value[4]*value[7] == req_prod:
            return 2
        elif value[2]*value[5]*value[8] == req_prod:
            return 2
        elif value[3]*value[6]*value[9] == req_prod:
            return 2
        
        #DIAGNOL CHECK
        
        if value[1]*value[5]*value[9] == req_prod:
            return 2
        elif value[3]*value[5]*value[7] == req_prod:
            return 2
        
        return 0
    else:
        req_prod = 27
        
        #HORIZONTAL CHECK
        
        if value[1]*value[2]*value[3] == req_prod:
            return 2
        elif value[4]*value[5]*value[6] == req_prod:
            return 2
        elif value[7]*value[8]*value[9] == req_prod:
            return 2
        
        #VERTICAL CHECK
        
        if value[1]*value[4]*value[7] == req_prod:
            return 2
        elif value[2]*value[5]*value[8] == req_prod:
            return 2
        elif value[3]*value[6]*value[9] == req_prod:
            return 2
        
        #DIAGNOL CHECK
        
        if value[1]*value[5]*value[9] == req_prod:
            return 2
        elif value[3]*value[5]*value[7] == req_prod:
            return 2
        
        return 0

                   
def play():
    turn = 1
    result = 0
    board, value = create_board()
    ans = input('do you wanna start(y/n)?')
    if ans == 'y':
        computer_value = 2
        PL_Mark = 'X'
        while(turn<10): 
            pos = player_input(board)  
            board[pos] = PL_Mark
            value[pos] = 5
            DrawBoard(board)
            
            result = player_win(value,1)
            if result == 2:
                print('You win')
                break
                
            turn += 1
            print(turn)
            result = GO(board,value,turn,computer_value)
            DrawBoard(board)
            if result != 0:
                print('Computer Wins')
                break
            turn += 1
            
            
    if ans == 'n':
        computer_value = 1
        PL_Mark = 'O'
        while(turn<10):     
            result = GO(board,value,turn,computer_value)
            DrawBoard(board)
            if result == 1:
                print('Computer Wins')
                break
            turn += 1
            pos = player_input(board)
            board[pos] = PL_Mark
            value[pos] = 3
            if turn == 10:
                break
            result = player_win(value,2)
            
            if result == 2:
                print('You win')
                break
            turn += 1
            print(turn)
            DrawBoard(board)
    if result == 0:
        print('Its a draw')
    

play()                
