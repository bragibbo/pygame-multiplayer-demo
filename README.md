# pygame-multiplayer-demo
This is a simple pygame multiplayer demo that was cobbled together in a few hours. It is not meant to be fully featured. It is not using the best design patterns for multiplayer state management.

## Demo Success Criteria
The purpose of this demo was to dive a little deeper into UDP networking in python and how that could be used to maintain the state of game objects across clients. This is not intended to be a full game. The success criteria was being able to update the position of a player accross two clients. Due to the way this demo was built, the server technically supports and unlimited number of clients. However, I would advise against this because of hardware and performance limitations. Also, this demo does not distinguish between game sessions. Only on a restart of the server will the game session be cleared. This artifact can be seen by the existance of dead player objects in a client session if a client has disconnected and the server was not restarted. Again, this features was outside the scope of the intended purpose of this demo. This is built to only work as a local multiplayer connection.

## Instructions
- Clone the repo
    ```
    git clone https://github.com/bragibbo/pygame-multiplayer-demo.git
    ```
- Navigate inside the project directory
    ```
    cd pygame-multiplayer-demo
    ```
- Install python 3: https://www.python.org/downloads/
- Install pip: https://pypi.org/project/pip/
- Install pygame
    ```
    pip install pygame
    ```
- Run the server (in the /server directory)
    ```
    cd server
    python3 main.py
    ```
- In a new terminal session, navigate to the /client, and run the client (repeat this step to connect additional clients)
    ```
    cd client
    python3 main.py
    ```
