#XnOs
#Zuhayr Loonat

#modules
import tkinter as tk

#variables (global)
scorep1 = 0
scorep2 = 0

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
move_choices = ["X","O","X","O","X","O","X","O","X"]

turn = "Player 1's Turn"
moves = 0
rounds = 0


#create board
#window
window = tk.Tk()
window.title("TicTacToe")
window.configure(background="#222221")
window.geometry("400x600")
window.resizable(False, False)

#lines and canvas for board
canvas=tk.Canvas(window, width=300, height=300)
canvas.configure(bg='#222221')
canvas.place(x=50, y=200)

canvas.create_line(10,100,295,100, fill="white", width=3)
canvas.create_line(10,200,295,200, fill="white", width=3)

canvas.create_line(100,10,100,295, fill="white", width=3)
canvas.create_line(200,10,200,295, fill="white", width=3)

#labels and canvas for top

info=tk.Canvas(window, width= 396, height=130)
info.config(bg='#222221')
info.place(y=2)

info.create_line(200,2,200,134, fill="white", width=2.5)

player1 = tk.Label(window, text="Player 1", font = "Arial 20 ")
player1.configure(bg="#222221", fg="white")
player1.place(x=50, y=5)

player2 = tk.Label(window, text="Player 2", font = "Arial 20 ")
player2.configure(bg="#222221", fg="white")
player2.place(x=250, y=5)

l_score1 = tk.Label(window, text=str(scorep1), font = "Arial 40 ")
l_score1.config(bg="#222221", fg="white")
l_score1.place(x = 85, y = 50)

l_score2 = tk.Label(window, text=str(scorep2), font = "Arial 40 ")
l_score2.config(bg="#222221", fg="white")
l_score2.place(x = 285, y = 50)

l_turn = tk.Label(window, text=turn, font = "Arial 20 ")
l_turn.config(bg="#222221", fg="white")
l_turn.place(x = 100, y = 150)
#buttons on board
b00 = tk.Button(window, text=board[0][0], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b01 = tk.Button(window, text=board[0][1], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b02 = tk.Button(window, text=board[0][2], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b10 = tk.Button(window, text=board[1][0], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b11 = tk.Button(window, text=board[1][1], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b12 = tk.Button(window, text=board[1][2], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b20 = tk.Button(window, text=board[2][0], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b21 = tk.Button(window, text=board[2][1], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

b22 = tk.Button(window, text=board[2][2], font = "Arial 30 bold", bg="#222221", fg="white", width = 3, height = 1)

#utility_buttons
b_restart = tk.Button(window, text="Start", font = "Arial 20 bold", bg="#222221", fg="white")


#GAME CODE
def gameplay():
    global scorep1, scorep2, moves, rounds, turn, board



    #cases for wins
    if ((board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or
        (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or
        (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or
        
        (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or
        (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or
        (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or

        (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or
        (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X')):

        if rounds%2==0:
            scorep1 += 1
        else: scorep2 +=1

        end_game()
    
    if ((board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or
        (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or
        (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or
        
        (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or
        (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or
        (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or

        (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or
        (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):

        if rounds%2==0:
            scorep2 += 1
        else: scorep1 +=1

        end_game()

    elif moves == 9: first_switch()


#end game
def end_game():
    global scorep1, scorep2

    if scorep1 == 10:
        refresh_score(scorep1, scorep2)
        hide_buttons()
        refresh_turn()
    elif scorep2 == 10:
        refresh_score(scorep1, scorep2)
        hide_buttons()
        refresh_turn()
    else:
        refresh_turn()
        first_switch()



#functions
def set_board():
    b00.config(text = "")
    b01.config(text = "")
    b02.config(text = "")
    b10.config(text = "")
    b11.config(text = "")
    b12.config(text = "")
    b20.config(text = "")
    b21.config(text = "")
    b22.config(text = "")

def refresh_turn():
    if (rounds%2 == 0 and moves%2 ==0) or (rounds%2 ==1 and moves%2 == 1):
        turn = "Player 1's Turn"
    else: turn = "Player 2's Turn"

    if scorep1 == 10:
        turn = "Player 1 Won"
    if scorep2 == 10:
        turn = "Player 2 Won"

    l_turn.config(text=turn)

def refresh_score(p1,p2):
    l_score1.config(text=str(p1))
    l_score2.config(text=str(p2))

    l_score1.place(x = 85, y = 50)
    l_score2.place(x = 285, y = 50)

def start_game():

    global moves, turn, rounds
    global scorep1, scorep2
    global board

    b_restart.config(text="Restart")
    b_restart.place(x = 140, y = 525)


    board=[[" "," "," "],[" "," "," "],[" "," "," "]]
    scorep1 = 0
    scorep2 = 0
    moves =0
    rounds = 0
    turn = "Player 1's Turn"
    set_board()
    refresh_score(0, 0)

    b00.place(x = 60, y = 210)
    b01.place(x = 160, y = 210)
    b02.place(x = 260, y = 210)
    b10.place(x = 60, y = 310)
    b11.place(x = 160, y = 310)
    b12.place(x = 260, y = 310)
    b20.place(x = 60, y = 410)
    b21.place(x = 160, y = 410)
    b22.place(x = 260, y = 410)

def hide_buttons():
    b00.place_forget()
    b01.place_forget()
    b02.place_forget()
    b10.place_forget()
    b11.place_forget()
    b12.place_forget()
    b20.place_forget()
    b21.place_forget()
    b22.place_forget()

def first_switch():
    global board
    global scorep1, scorep2, rounds, moves

    rounds +=1
    moves = 0

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    set_board()
    refresh_score(scorep1, scorep2)

def make_move(letter,button):
    button.config(text=letter)
    global moves
    moves += 1

    gameplay()
    refresh_turn()
    

def set_position(letter,button):

    if button == b00:
        board[0][0]=letter
    if button == b01:
        board[0][1]=letter
    if button == b02:
        board[0][2]=letter
    if button == b10:
        board[1][0]=letter
    if button == b11:
        board[1][1]=letter
    if button == b12:
        board[1][2]=letter
    if button == b20:
        board[2][0]=letter
    if button == b21:
        board[2][1]=letter
    if button == b22:
        board[2][2]=letter
    
    make_move(letter, button)


#button behaviour
b_restart.config(command=lambda : start_game())

b00.config(command=lambda : set_position(move_choices[moves],b00))
b01.config(command=lambda : set_position(move_choices[moves],b01))
b02.config(command=lambda : set_position(move_choices[moves],b02))
b10.config(command=lambda : set_position(move_choices[moves],b10))
b11.config(command=lambda : set_position(move_choices[moves],b11))
b12.config(command=lambda : set_position(move_choices[moves],b12))
b20.config(command=lambda : set_position(move_choices[moves],b20))
b21.config(command=lambda : set_position(move_choices[moves],b21))
b22.config(command=lambda : set_position(move_choices[moves],b22))
#button packings
b_restart.place(x = 155, y = 525)


#game code run
window.mainloop()

