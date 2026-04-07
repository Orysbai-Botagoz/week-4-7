#4 task
class Inventory:
    def __init__(self):
        self._items = []
    def add_item(self, item):
        if not any(existing_item.id == item.id for existing_item in self._items):
            self._items.append(item)
    def remove_item(self, item_id: int):
        self._items = [item for item in self._items if item.id != item_id]
    def get_items(self) -> list:
        return self._items
    def unique_items(self) -> set:
        return set(self._items)
    def to_dict(self) -> dict:
        return {item.id: item for item in self._items}
    #18 task
    def __iter__(self):
        return iter(self._items)
# 5 task
    def get_strong_items(self, min_power: int) -> list:
        check_power = lambda item: item.power >= min_power
        return [item for item in self._items if check_power(item)]
inv = Inventory()
strong_items = [item for item in inv if item.power > 50]


#1 task
from tkinter import EventType


class Player:
    def __init__(self, _id, _name, _hp):
        self._id = _id
        self._name = _name.strip().title()
        self._hp = max(0, _hp)
        self._inventory = Inventory()

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

    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)
    @property
    def inventory(self):
        return self._inventory





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
    def __repr__(self): #set ті көруге ыңғайлы
        return f"Item(id={self.id}, name='{self.name}', power={self.power})"


#6 task
from datetime import datetime
class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def __str__(self):
        return f'Event(type={self.type}, data={self.data}, timestamp={self.timestamp})'



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


#10 task
class EventIterator:
    def __init__(self, events: list[Event]):
        self.events = events
        self.index = 0
        pass
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.events):
            event = self.events[self.index]
            self.index += 1
            return event
        else:
            raise StopIteration

#11 task
def damage_stream(events: list[Event]): #генератор чтоб экономить память
    for event in events:
        if event.type == "ATTACK":
            yield event.data["damage"]
        pass

#12 task
import random
def generate_events(players: list[Player], items: list[Item], n: int) -> list[Event]:
    get_random_event = lambda: random.choice(["ATTACK", "LOOT"])
    all_events = []
    for player in players:
        for _ in range(n):
            e_type = get_random_event()
            if e_type == "LOOT":
                e_data = {"item": random.choice(items)}
            elif e_type == "ATTACK":
                e_data = {"damage": random.randint(1, 100)}
            new_event = Event(e_type, e_data)
            all_events.append(new_event)
    return all_events
    pass

#13 task
def analyze_logs(events: list[Event]) -> dict:
    if not events:
        return {"total_damage": 0, "top_player": "None", "most_common_event": "None"}
    counts = {}
    total_damage = 0
    player_damage = {}
    for e in events:
        counts[e.type] = counts.get(e.type, 0) + 1
        if e.type == "ATTACK":
            damage_val = int(e.data.get("damage", 0))
            total_damage += damage_val
            player_name = "Simulation Player"
            if "player" in e.data:
                p = e.data["player"]
                player_name = getattr(p, "_name", str(p))
            player_damage[player_name] = player_damage.get(player_name, 0) + damage_val
    most_common_event = max(counts, key=counts.get) if counts else "None"
    top_player = max(player_damage, key=player_damage.get) if player_damage else "No combat"
    return {
        "total_damage": total_damage,
        "top_player": top_player,
        "most_common_event": most_common_event,
    }

#14 task
decide_action = lambda p: "ATTACK" if p._hp >= 30 and p.inventory.items else("HEAL" if p._hp < 30 else "LOOT")

#7 and 15 task
class Warrior(Player):
    def handle_event(self, event: Event):
        if event.type == "ATTACK":
            damage = event.data["damage"]
            damage *= 0.9
            self._hp = max(self._hp - damage, 0)
        else:
            super().handle_event(event)
class Mage(Player):
    def handle_event(self, event: Event):
        if event.type == "LOOT":
            item = event.data.get("item")
            if item:
                item.power *= 1.1
                self.inventory.add_item(item)
        else:
            super().handle_event(event)
        pass
        super().handle_event(event)

#19 task
def analyze_inventory(inventory: Inventory) -> dict:
    items = list(inventory)
    if not items:
        return {"unique_items": set(), "top_power": None}
    unique_items = set(items)
    top_power_item = max(items, key=lambda item: item.power)
    return {
        "unique_items": unique_items, # set уникальных предметов
        "top_power": top_power_item, #предмет с наибольшей силой
    }

#20 task
def main():
    warrior = Warrior(1, "Konan", 120)
    mage = Mage(2, "Gandalf", 80)
    players = [warrior, mage]
    items = [
        Item(101, "Axe", 40),
        Item(102, "Staff", 60),
        Item(103, "Shield", 30)
    ]
    all_events = generate_events(players, items, 5)
    log_file = "game_logs.txt"
    open(log_file, "w").close()
    for event in all_events:
        for player in players:
            player.handle_event(event)
            Logger.log(event, player, log_file)
    loaded_events = Logger.read_logs(log_file)
    print("=== ФИНАЛЬНАЯ СИМУЛЯЦИЯ АЯҚТАЛДЫ ===")
    top_collector = max(players, key=lambda p: len(p.inventory.get_items()))
    print(f"Максималды зат саны бар ойыншы: {top_collector._name} ({len(top_collector.inventory.get_items())} зат)")
    try:
        stats = analyze_logs(loaded_events)
        print(f"Ең көп зиян келтірген: {stats['top_player']}")
        print(f"Жалпы статистика: {stats['most_common_event']} оқиғасы ең көп болды")
    except Exception as e:
        print(f"Аналитика кезінде қате: {e}")
    for p in players:
        p_stats = analyze_inventory(p.inventory)
        if p_stats['top_power']:
            print(f"{p._name} инвентарындағы ең күшті зат: {p_stats['top_power'].name}")
        else:
            print (f"{p._name} инвентары бос.")
if __name__ == "__main__":
        main()