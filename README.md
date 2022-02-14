# Information
This is a Client server program written in python 3.8 (because why would someone choose java for this??) that allows a user on a client side to command's to the server and receive the results back from the server over TCP. The program also takes advantage of using regular expressions to search for matches in the message the client sends over to the server.
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
Starting with no files made to store the users solved commands and only a file to keep track of who can log in we'll go through each command looking at the output.
   1. LOGIN root root22 and LOGIN sally sally33                                                                                                                  
   ![Screenshot from 2022-02-13 20-30-44](https://user-images.githubusercontent.com/69600850/153786188-81aa2233-7226-473d-b600-76732e822c8f.png)  <br>
   ![Screenshot from 2022-02-13 20-33-32](https://user-images.githubusercontent.com/69600850/153785942-ed6fda4b-3330-4722-8663-a3d10c093236.png)  
Now we know we can log in, lets issue four solve commands. One while signed into root, one signed into john,one signed into qiang and one in qiang
  2. SOLVE -r 7 7, SOLVE -c 10, SOLVE -r 6 , and SOLVE -ghds 5g
  ![Screenshot from 2022-02-13 20-49-26](https://user-images.githubusercontent.com/69600850/153786705-06a990fe-615f-4a31-83ad-93aa4b9b0d1c.png)  
  ![Screenshot from 2022-02-13 20-52-39](https://user-images.githubusercontent.com/69600850/153786909-ba9cc518-2275-42f4-9f7a-519a12a87b15.png)   
  ![Screenshot from 2022-02-13 20-56-17](https://user-images.githubusercontent.com/69600850/153787082-98fe7a2d-b27a-4c00-ae71-7889d04a4080.png)  
  ![Screenshot from 2022-02-13 20-58-17](https://user-images.githubusercontent.com/69600850/153787241-607f77fc-743c-4f0f-b18f-afc770e8ac8f.png)
