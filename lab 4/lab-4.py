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
    def handle_event(self, event: 'Event'):
        if event.type == "ATTACK":
            damage = event.data.get("damage", 0)
            self.hp = max(0, self._hp - damage)
        elif event.type == "HEAL":
            amount = event.data.get("amount", 0)
            self._hp += amount
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
mage.handle_event(loot_event)
print(f"Здоровье мага: {mage._hp}")
items = mage.inventory.get_items()
print(f"Количество предметов в инвентаре: {len(items)}")

if items:
    found_item = items[0]
    print(f"Предмет: {found_item.name}")
    print(f"Финальная сила (с учетом бонуса мага 10%): {found_item.power}")

#8 task
import ast
class Logger:
    @staticmethod
    def log(event: Event, player: Player, file_name: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        readable_data = {k: str(v) for k, v in event.data.items()}
        with open(file_name, "a") as f:
            f.write(f"{event.timestamp};{player._id};{event.type};{readable_data}\n")
        pass

#9 task
    def read_logs(filename: str) -> list[Event]:
        events = []
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    parts = line.split(";")
                    if len(parts) < 4:
                        continue
                    e_type = parts[2]
                    e_data = ast.literal_eval(parts[3]) #тексттті диктке
                    new_event = Event(e_type, e_data)
                    events.append(new_event)
                    pass
        except FileNotFoundError:
            return []
        return events


tester_mage = Mage(10, "Moira", 80)
magic_wand = Item(1, "Magic Wand", 15)
loot_event = Event("LOOT", {"item": magic_wand})

# 2. Записываем событие в файл
file_name = "test_game.log"
Logger.log(loot_event, tester_mage, file_name)

# 3. Читаем логи и проверяем результат
restored_events = Logger.read_logs(file_name)

if restored_events:
    last_event = restored_events[-1]
    print(f"✅ Тип события: {last_event.type}")
    print(f"✅ Данные события: {last_event.data}")

    # Проверим, что данные превратились обратно в словарь
    if isinstance(last_event.data, dict):
        print("🚀 Успех: Данные снова стали словарем!")