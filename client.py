
from socket import *
from tkinter import *
from tkinter import messagebox
import threading

try:
    
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_number = int(client_socket.recv(1024).decode())
    
    def send():
        guess = guess_field.get()
        client_socket.send(guess.encode())
        if int(guess) < client_number:
            player_one_Status.config(text="Too low!")
        elif int(guess) > client_number:
            player_one_Status.config(text="Too high!")
        else:
            player_one_Status.config(text="correct \nplayer 2 \"win\"")
            messagebox.showinfo("Game Result", "player 2 win!")
        guess_button.config(state=DISABLED)


    def receive():
        while True:
            guess_2 = client_socket.recv(1024).decode()
            player_two_guess.config(text=guess_2)
            if int(guess_2) < client_number:
                player_two_Status.config(text="Too low!")
            elif int(guess_2) > client_number:
                player_two_Status.config(text="Too high!")
            else:
                player_two_Status.config(text="correct  \nplayer 1 \"win\"")
                guess_button.config(state=DISABLED)
                messagebox.showinfo("Game Result", "player 1 win!")
                break
            guess_button.config(state=NORMAL)

    t = threading.Thread(target=receive, args=())
    t.start()
    # Initialize the game window
    window = Tk()
    window.title("Guess the Number")
    window.geometry("400x400")
    # Create the UI elements
    title_label = Label(
        window, text="Guess the Number From 1 : 100 \nplayer 2 :", font=15)
    title_labe2 = Label(window, text="player 1 :",
                        font=18, justify="center")
    player_two_guess = Label(window, text="0",
                             font=("Arial", 20), fg='red', justify="center")
    player_two_Status = Label(window, text="no status",
                              font=("Arial", 16), fg='red', justify="center")
    player_one_Status = Label(window, text="waiting",
                              font=("Arial", 16), fg='red', justify="center")
    guess_field = Entry(window, width=10, font=("Arial", 14))
    guess_button = Button(window, text="Guess", command=send)

    # Add the UI elements to the window
    title_label.place(x=60, y=20)
    title_labe2.place(x=160, y=200)
    guess_field.place(x=140, y=80)
    guess_button.place(x=270, y=80)
    player_two_guess.place(x=180, y=240)
    player_two_Status.place(x=155, y=280)
    player_one_Status.place(x=150, y=120)
    # Start the game
    window.mainloop()

    client_socket.close()  # client close the socket connection with server
except error as e:
    print(e)
#-------------------------------------------------------------

