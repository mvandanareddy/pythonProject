from tkinter import *
from tkinter import messagebox
import random as r


def button(frame):
    b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial', 60, 'bold'), relief="sunken", bd=10)
    return b


def change_a():  # Function to change the operand for the next player
    global a
    for i in [player1, player2]:
        if not (i == a):
            a = i
            break


def reset():  # Resets the game
    global a
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL
    a = r.choice(['O', 'X'])


def check():  # Checks for victory or Draw
    for i in range(3):
        if (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == names[player1] or b[0][i]["text"] == b[1][i][
            "text"] == b[2][i]["text"] == names[player1]):
            messagebox.showinfo("Congrats!!", "'" + player1 + "' has won")
            play = messagebox.askquestion(title="check", message="do you want to play again?")
            if play == "yes":
                reset()
            else:
                for i in range(3):
                    for j in range(3):
                        b[i][j]["state"] = DISABLED
                return
        elif (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == names[player2] or b[0][i]["text"] == b[1][i][
            "text"] == b[2][i]["text"] == names[player2]):
            messagebox.showinfo("Congrats!!", "'" + player2 + "' has won")
            play = messagebox.askquestion(title="check", message="do you want to play again?")
            if play == "yes":
                reset()
            else:
                for i in range(3):
                    for j in range(3):
                        b[i][j]["state"] = DISABLED
                return

    if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == names[player1] or b[0][2]["text"] == b[1][1]["text"] ==
            b[2][0]["text"] == names[player1]):
        messagebox.showinfo("Congrats!!", "'" + player1 + "' has won")
        play = messagebox.askquestion(title="check", message="do you want to play again?")
        if play == "yes":
            reset()
        else:
            for i in range(3):
                for j in range(3):
                    b[i][j]["state"] = DISABLED
        return
    elif (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == names[player2] or b[0][2]["text"] == b[1][1][
        "text"] == b[2][0]["text"] == names[player2]):
        messagebox.showinfo("Congrats!!", "'" + player2 + "' has won")
        play = messagebox.askquestion(title="check", message="do you want to play again?")
        if play == "yes":
            reset()
        else:
            for i in range(3):
                for j in range(3):
                    b[i][j]["state"] = DISABLED
        return


    elif (b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] == b[1][2][
        "state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED):
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        play = messagebox.askquestion(title="check", message="do you want to play again?")
        if play == "yes":
            reset()
        else:
            for i in range(3):
                for j in range(3):
                    b[i][j]["state"] = DISABLED
        return


def click(row, col):
    if mode == 2 or a != "Computer":
        b[row][col].config(text=names[a], state=DISABLED, disabledforeground=colour[a])
    else:
        l = []
        for i in range(3):
            for j in range(3):
                if b[i][j]["text"].strip() == "":
                    l.append([i, j])
        new = r.choice([x for x in l])
        b[new[0]][new[1]].config(text=names[a], state=DISABLED, disabledforeground=colour[a])

    res = check()
    if res != 1:
        change_a()
        label.config(text=a + "'s Chance")


###############   Main Program #################
ii = 0

mode = int(input("Select your choice:\n1 To play with computer\n2 For local play\n--->"))

# Repeating the loop until user enters mode from given list
while ii == 0:
    if mode not in [1, 2]:
        mode = int(input("Please select 1 or 2 :"))
    else:
        ii = 1
player1 = input("Player 1 enter your name:")  # Taking name of player1
if mode == 2:
    player2 = input("Player 2 enter your name:")  # Taking name of player2
else:
    player2 = "Computer"  # Making computer as a player

root = Tk()  # Window defined

e = Entry(root)
print(e)

root.title("TIC-TAC-TOE")  # Title given
a = r.choice([player1, player2])  # Two operators defined
names = {player1: "O", player2: "X"}
colour = {player1: "deep sky blue", player2: "lawn green"}
b = [[], [], []]
for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)
label = Label(text=a + "'s Chance", font=('arial', 20, 'bold'))
label.grid(row=3, column=0, columnspan=3)
root.mainloop()