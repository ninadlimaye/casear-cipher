# casear-cipher

Server.py initiates a socket connection and waits for any client(can be a local or remote) to connect to it. After a client is connected, it binds to the client to listen for data. The code consists a Caesar Cipher function that returns the translated message with a shift size of positive or negative integer.

Client.py connects to the server.py and then sends the message to be translated. The translated message is sent to the client from the server.
