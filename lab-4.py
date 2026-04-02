#1 task
from tkinter import EventType


class Player:
    def __init__(self, _id, _name, _hp):
        self._id = _id
        self._name = _name.strip().title()
        self._hp = max(0, _hp)
        self.inventory = Inventory()

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
    #continue 7 task
    def handle_event(self, event: event):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.hp = max(0, self._hp - damage)
        elif event.type == "HEAL":
            amount = event.data.get("amount", 0)
            self.hp += amount
        elif event.type == "LOOT":
            item = event.data.get("item")
            if item:
                self.inventory.add_item(item)


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
p = Player.from_string("2, alice , 90")
print(p)

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
i = Item(1, " Sword ", 50)
print(i)

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

#6 task
from datetime import datetime
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def __str__(self):
        return f'Event(type={self.type}, data={self.data}, timestamp={self.timestamp})'

e = Event("ATTACK", {"damage": 20})
print(e)

#7 task
class Warrior(Player):
    def handle_event(self, event: Event):
       if event.type == "ATTACK":
           resuced_damage = event.data.get("damage", 0) * 0.9
           self._hp = max(0, self._hp - resuced_damage)
           pass
       else:
           super().handle_event(event)
class Mage(Player):
    def handle_event(self, event: Event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power *= 1.1
            super().handle_event(event)
            pass
        else:
            super().handle_event(event)
mage = Mage(1, "Gandalf", 100)
staff = Item(10, "Magic Staff", 50)
loot_event = Event("LOOT", {"item": staff})

