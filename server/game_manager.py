import uuid


class GameManager:
    def __init__(self):
        self.connected_clients = {}
        self.game_state = {}

    def handle_request(self, data, address):
        if address not in self.connected_clients:
            self.connected_clients[address] = str(uuid.uuid4())
            print("Connected client {} from address {}".format(self.connected_clients[address], address))

        res = {"client_id": self.connected_clients[address]}
        res = self.update(data, res)
        return self.connected_clients, res

    # Replace with match case once you update to python 3.10
    def update(self, data, res):
        if data["state"] == "CONNECT":
            print("Finishing connection")
        if data["state"] == "DISCONNECT":
            del self.connected_clients[data["client_id"]]
        if data["state"] == "UPDATE_PLAYER_POSITION":
            self.update_player_position(data["client_id"], data["new_x"], data["new_y"])
            res["player_position"] = self.game_state["player_position"]
        return res

    def update_player_position(self, client_id, new_x, new_y):
        if "player_position" not in self.game_state:
            self.game_state["player_position"] = {}
        if client_id not in self.game_state:
            self.game_state["player_position"][client_id] = {}
        self.game_state["player_position"][client_id]["x_pos"] = new_x
        self.game_state["player_position"][client_id]["y_pos"] = new_y
