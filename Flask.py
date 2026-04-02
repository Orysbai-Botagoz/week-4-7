from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    return "Сервер жұмыс істеп тұр"

@app.route('/sum')
def sum_ab():
    a = 7
    b = 3
    return str(a + b)

#1 task
class player:
    def __init__(self, _id, _name, _hp):
        self._id = _id
        self._name = _name.strip().title()
        self._hp = max(0, _hp)

    def __str__(self):
        return f"Player(id={self._id}, name='{self._name}', hp={self._hp}')"

    def __del__(self):
        # Серверде бұл тек консольге шығады
        print(f"Player {self._name} жойылды")

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'hp': self._hp,
        }

#2 task
    @classmethod
    def from_string(cls, data: str):
        try:
            parts = [item.strip() for item in data.split(",")]
            if len(parts) == 3:
                return cls(int(parts[0]), str(parts[1]), int(parts[2])) #Создает и возвращает нового игрока.
            else:
                return None
        except (ValueError, IndexError): #Если формат неверный
            raise ValueError("Неверный формат строки") #Принудительный вызов ошибки

#3 task
class Item:
    def __init__(self, id, name, power):
        self.id = id
        self.name = name.strip()
        self.power = power
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'power': self.power,
        }

    def __str__(self):
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"
    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.id == other.id
    def __hash__(self):
        return hash(self.id)

#4 task
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        if not any(existing_item.id == item.id for existing_item in self.items):
            self.items.append(item)
    def remove_item(self, item_id: int):
        self.items = [item for item in self.items if item.id != item_id]
    def get_items(self) -> list:
        return self.items
    def unique_items(self) -> set:
        return set(self.items)
    def to_dict(self) -> dict:
        return {item.id: item for item in self.items}

#5 task
    def get_strong_items(self, min_power: int) -> list:
        check_power = lambda item: item.power >= min_power
        return [item for item in self.items if check_power(item)]

my_inventory = Inventory()
my_inventory.add_item(Item(1, "Sword", 50))
my_inventory.add_item(Item(2, "Shield", 100))
my_inventory.add_item(Item(3, "John", 120))
my_inventory.add_item(Item(4, "Tina", 200))
@app.route("/inventory/all")
def get_all():
    return jsonify([i.to_dict() for i in my_inventory.get_items()])

#1 task
@app.route("/player_data")
def player_data_route():
    p1 = player(1, " john ", 120)
    return jsonify(p1.to_dict())

#2 task
@app.route('/player_dict')
def player_dict_route():
    p = player.from_string("2, alice , 90")
    if p is None:
        return jsonify({"error": "Деректер форматы қате"}), 400
    return jsonify(p.to_dict())

#3 task
@app.route('/Item')
def item_route():
    i = Item(1, " Sword ", 50)
    return jsonify(i.to_dict())

#4 and 5 task
@app.route('/test_inventory')
def test_inventory():
    inv = Inventory()
    inv.add_item(Item(1, "John", 10))
    inv.add_item(Item(2, "Assem", 100))
    inv.add_item(Item(3, "Tina", 150))
    strong_ones = inv.get_strong_items(50)
    return jsonify([i.to_dict() for i in strong_ones])



if __name__ == '__main__':
    # debug=True қателерді көруге көмектеседі
    app.run(port=9000, debug=True)