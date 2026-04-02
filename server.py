from flask import Flask, request, jsonify
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)
@app.route('/')
def home():
    return "Сервер работает"
@app.route('/sum')
def sum_ab():
    a = 7
    b = 3
    c = a + b
    return str(c)

class player:
    def __init__(self, _id, _name, _hp):
        self._id = _id
        self._name = _name.strip().title()
        self._hp = max(0, _hp)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp}')"

    def __del__(self):
        print(f"Player {self._name} удалён")

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self._name,
            'hp': self._hp,
        }

    @classmethod
    def from_string(cls, data: str):
        parts = [item.strip() for item in data.split(",")]
        if len(parts) == 3:
            return cls(int(parts[0]), str(parts[1]), int(parts[2]))
        else:
            raise ValueError

@app.route("/player_data")
def player_data():
    p = player(1, " john ", 120)
    return jsonify(p.to_dict())
@app.route('/player_dict')
def player_dict():
    p = player.from_string("2, alice , 90")
    return jsonify(p.to_dict())




if __name__ == '__main__':
    app.run(port=8002)