# Information
This is a Client server program written in python 3.8 (because why would someone choose java for this??) that allows a user on a client side to command's to the server and receive the results back from the server over TCP. 
Currently, the commands implemented are:
  1. LOGIN
  2. SOLVE
  3. LIST
  4. LIST -all
  5. LOGOUT
  6. SHUTDOWN

# Building and running the program 
Running the program is the same no matter what machine you are running it on. First you have to run the server before you can run the client. Once the Server is running, you can start up the client to connect to the server, and then you are free to dish out commands to the sever!

# Known bugs 
At the moment, there are 2 bugs. The first one is the root user can run the `LIST -all` command, but it only outputs the solved commands the root user has sent to the sever and nobody else.  
# Output
