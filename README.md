# Guess-The-Number-Game-
My game is a simple "Guess the Number" game implemented using client-server architecture with socket programming. Here's a description of the game and how it was built:

Description of the Game:
The game involves two players, Player 1 and Player 2.
Player 1 runs the server code, and Player 2 runs the client code.
Player 1 (server) generates a random number between 1 and 100 and sends it to Player 2 (client).
Player 2 (client) receives the random number and starts guessing the number.
Player 1 (server) waits for Player 2's guess and provides feedback (too high, too low, correct guess) based on the guessed number.
Player 2 (client) continues guessing until they guess the correct number.
The game ends when either Player 1 (server) or Player 2 (client) guesses the correct number.
How it was Built using Socket Programming:
Server Side (Player 1):

The server code is responsible for generating the random number and listening for incoming connections from clients.
It uses the socket module to create a TCP socket and binds it to a specific address and port.
After binding, the server listens for incoming connections using the listen() method.
Once a client connects, the server accepts the connection using the accept() method.
It then sends the randomly generated number to the client.
The server continuously receives guesses from the client and provides feedback until the game ends.
Client Side (Player 2):

The client code connects to the server using the server's address and port.
After connecting, the client receives the random number sent by the server.
It then allows the player to input guesses via a GUI interface.
The client sends the guess to the server, receives feedback, and displays it to the player.
The client continues this process until the game ends.
Communication:

Communication between the client and server is achieved using sockets.
The socket module is used to create sockets on both the client and server sides.
The send() and recv() methods are used to send and receive data between the client and server.
Both client and server handle sending and receiving data asynchronously using threads to ensure responsiveness.
GUI (Graphical User Interface):

The game interface is implemented using the Tkinter library in Python.
Tkinter provides a simple way to create graphical interfaces for Python applications.
Labels, buttons, and entry fields are used to create the UI elements for the game.
GUI elements are updated based on the feedback received from the server or client during the game.
Overall, the game leverages socket programming to enable communication between the client and server, allowing for an interactive "Guess the Number" game experience. The combination of socket programming and GUI implementation using Tkinter creates a multiplayer game where players can guess a random number and compete to win.
