class player:
    def __init__(self, name, health=100, attack_power=10, defense=5):
        self.name = name
        self._health = health
        self._attack_power = attack_power
        self._defense = defense
        self._inventory = []
        self._level = 1
        self._experience = 0
        self.position = (0, 0)  # x, y coordinates
        self.is_alive = True

    def attack(self, target):
        if self.is_alive:
            damage = self._attack_power - target._defense
            damage = max(damage, 0)  # Ensure damage is not negative
            target._health -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            if target._health <= 0:
                target.is_alive = False
                target._health = 0
                print(f"{target.name} has been defeated!")
        else:
            print(f"{self.name} cannot attack because they are not alive.")

    def heal(self, amount):
        if self.is_alive:
            self._health += amount
            self._health = min(self._health, 100)  # Cap health at 100
            print(
                f"{self.name} heals for {amount} points. Current health: {self._health}")
        else:
            print(f"{self.name} cannot heal because they are not alive.")

    def move(self, direction):
        if self.is_alive:
            x, y = self.position
            if direction == "up":
                self.position = (x, y + 1)
            elif direction == "down":
                self.position = (x, y - 1)
            elif direction == "left":
                self.position = (x - 1, y)
            elif direction == "right":
                self.position = (x + 1, y)
            print(f"{self.name} moves {direction}. New position: {self.position}")
        else:
            print(f"{self.name} cannot move because they are not alive.")

    def gain_experience(self, amount):
        if self.is_alive:
            self._experience += amount
            print(f"{self.name} gains {amount} experience points.")
            if self._experience >= 100:
                self.level_up()
                self._experience -= 100
        else:
            print(f"{self.name} cannot gain experience because they are not alive.")

    def level_up(self):
        self._level += 1
        self._attack_power += 5
        self._defense += 2
        self._health = 100
        print(f"{self.name} leveled up! New level: {self._level}")

    def add_to_inventory(self, item):
        if self.is_alive:
            self._inventory.append(item)
            print(f"{item} added to {self.name}'s inventory.")
        else:
            print(
                f"{self.name} cannot add items to inventory because they are not alive.")

    def show_status(self):
        status = f"Name: {self.name}\nHealth: {self._health}\nAttack Power: {self._attack_power}\nDefense: {self._defense}\nLevel: {self._level}\nExperience: {self._experience}\nPosition: {self.position}\nAlive: {self.is_alive}"
        print(status)

    def respawn(self):
        if not self.is_alive:
            self._health = 100
            self.is_alive = True
            self.position = (0, 0)
            print(f"{self.name} has respawned at the starting position.")
        else:
            print(f"{self.name} is already alive and cannot respawn.")

    def use_item(self, item):
        if self.is_alive:
            if item in self._inventory:
                self._inventory.remove(item)
                print(f"{self.name} uses {item}.")
                # Example effect of using an item
                if item == "health potion":
                    self.heal(20)
                elif item == "strength potion":
                    self._attack_power += 5
                    print(
                        f"{self.name}'s attack power increased to {self._attack_power}.")
                else:
                    print(f"{item} has no effect.")
            else:
                print(f"{item} is not in {self.name}'s inventory.")
        else:
            print(f"{self.name} cannot use items because they are not alive.")
            print(f"{self.name}'s current health: {self.health}")

    def take_damage(self, amount):
        if self.is_alive:
            self._health -= amount
            print(
                f"{self.name} takes {amount} damage. Current health: {self._health}")
            if self._health <= 0:
                self.is_alive = False
                self._health = 0
                print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} cannot take damage because they are not alive.")

    def reset(self):
        self._health = 100
        self._attack_power = 10
        self._defense = 5
        self.inventory = []
        self.level = 1
        self.experience = 0
        self.position = (0, 0)
        self.is_alive = True
        print(f"{self.name} has been reset to initial state.")

    def trade_item(self, item, target_player):
        if self.is_alive and target_player.is_alive:
            if item in self._inventory:
                self._inventory.remove(item)
                target_player.add_to_inventory(item)
                print(f"{self.name} trades {item} to {target_player.name}.")
            else:
                print(f"{item} is not in {self.name}'s inventory.")
        else:
            print("Both players must be alive to trade items.")

    def display_inventory(self):
        if self.is_alive:
            if self._inventory:
                print(f"{self.name}'s Inventory: {', '.join(self._inventory)}")
            else:
                print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name} cannot display inventory because they are not alive.")

    def equip_item(self, item):
        if self.is_alive:
            if item in self._inventory:
                print(f"{self.name} equips {item}.")
                # Example effect of equipping an item
                if item == "sword":
                    self.attack_power += 10
                    print(
                        f"{self.name}'s attack power increased to {self.attack_power}.")
                elif item == "shield":
                    self.defense += 5
                    print(f"{self.name}'s defense increased to {self.defense}.")
                else:
                    print(f"{item} has no effect when equipped.")
            else:
                print(f"{item} is not in {self.name}'s inventory.")
        else:
            print(f"{self.name} cannot equip items because they are not alive.")

    def flee(self):
        if self.is_alive:
            print(f"{self.name} flees from battle!")
            # Example effect of fleeing
            self.position = (0, 0)
            print(f"{self.name} has moved to the starting position: {self.position}")
        else:
            print(f"{self.name} cannot flee because they are not alive.")
            print(f"{self.name}'s current health: {self.health}")


class room:
    def __init__(self, description, items=None):
        self.description = description
        self.items = items if items else []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to the room.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from the room.")
        else:
            print(f"{item} is not in the room.")

    def show_items(self):
        if self.items:
            print("Items in the room:", ', '.join(self.items))
        else:
            print("The room is empty.")


player1 = player("Hero", health=100, attack_power=20, defense=5)
monster = player("Monster", health=80, attack_power=15, defense=3)
player3 = player("Sidekick", health=90, attack_power=10, defense=4)
player4 = player("Villain", health=120, attack_power=25, defense=6)
potion_room = room(
    "A small room with a healing potion on the table.", items=["health potion"])
sword_room = room(
    "A dark room with a shiny sword on the wall.", items=["sword"])
# Example interactions
player1.show_status()
player1.attack(monster)
monster.show_status()
monster.attack(player1)
player1.heal(15)
player1.move("up")
player1.gain_experience(120)
player1.add_to_inventory("health potion")
player1.show_status()
player1.use_item("health potion")
player1.show_status()
player1.trade_item("health potion", player3)
player3.display_inventory()
player1.equip_item("sword")
player1.show_status()
player1.flee()
player1.show_status()
player1.reset()
player1.show_status()
player1.show_status()
monster.show_status()
player1.attack(monster)
