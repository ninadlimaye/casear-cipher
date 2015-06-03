# casear-cipher
Virtual Security Research

Server.py initiates a socket connection and waits for client to connect to it. After a client is connected, it binds to the client to listen for data. It includes a function of Caesar Cipher that returns the new modified message with a shift size of positive or negative integer.

Client.py connects to the server.py and then sends the message to be modified. The modified message is returned back in the client from the server.

It is tested only on localhost machine.
