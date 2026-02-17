import random

# ==================== КЛАСС ПЕРСОНАЖА ====================
class Character:
    def __init__(self, race):
        self.race = race
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 100
        self.stat_points = 0
        
        # Генерация характеристик в зависимости от расы
        if race == "Человек":
            self.hp_max = random.randint(80, 100)
            self.attack = random.randint(10, 15)
            self.defense = random.randint(8, 12)
            self.agility = random.randint(10, 14)
            self.height = random.randint(160, 190)
            self.weight = random.randint(60, 90)
        elif race == "Эльф":
            self.hp_max = random.randint(70, 90)
            self.attack = random.randint(8, 12)
            self.defense = random.randint(6, 10)
            self.agility = random.randint(15, 20)
            self.height = random.randint(170, 200)
            self.weight = random.randint(50, 70)
        elif race == "Дворф":
            self.hp_max = random.randint(90, 120)
            self.attack = random.randint(12, 18)
            self.defense = random.randint(10, 15)
            self.agility = random.randint(5, 10)
            self.height = random.randint(130, 150)
            self.weight = random.randint(70, 100)
        
        # Текущие значения
        self.hp_current = self.hp_max
        self.coins = 0
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        
        # Применяем влияние роста и веса на характеристики
        self.apply_size_modifiers()
    
    def apply_size_modifiers(self):
        """Влияние роста и веса на ловкость"""
        # Высокие персонажи немного теряют ловкость
        if self.height > 180:
            self.agility -= 2
        # Тяжелые персонажи теряют ловкость
        if self.weight > 80:
            self.agility -= 1
    
    def get_total_attack(self):
        """Общая атака с учетом оружия"""
        weapon_bonus = 0
        if self.equipped_weapon:
            weapon_bonus = self.equipped_weapon["attack_bonus"]
        return self.attack + weapon_bonus
    
    def get_total_defense(self):
        """Общая защита с учетом брони"""
        armor_bonus = 0
        if self.equipped_armor:
            armor_bonus = self.equipped_armor["defense_bonus"]
        return self.defense + armor_bonus
    
    def show_stats(self):
        """Показать характеристики персонажа"""
        print("\n" + "="*50)
        print(f"ХАРАКТЕРИСТИКИ ПЕРСОНАЖА ({self.race})")
        print("="*50)
        print(f"Уровень: {self.level}")
        print(f"Опыт: {self.exp}/{self.exp_to_next_level}")
        print(f"Очки прокачки: {self.stat_points}")
        print(f"Здоровье: {self.hp_current}/{self.hp_max}")
        print(f"Атака: {self.attack} (+{self.get_total_attack() - self.attack} от оружия)")
        print(f"Защита: {self.defense} (+{self.get_total_defense() - self.defense} от брони)")
        print(f"Ловкость: {self.agility}")
        print(f"Рост: {self.height} см, Вес: {self.weight} кг")
        print(f"Монеты: {self.coins}")
        print("="*50)
    
    def gain_exp(self, amount):
        """Получить опыт"""
        self.exp += amount
        print(f"\nВы получили {amount} опыта!")
        
        # Проверка повышения уровня
        while self.exp >= self.exp_to_next_level:
            self.level_up()
    
    def level_up(self):
        """Повышение уровня"""
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)
        self.stat_points += 3
        self.hp_max += 10
        self.hp_current = self.hp_max
        
        print(f"\n Поздравляем! Вы достигли {self.level} уровня!")
        print(f"Получено 3 очка характеристик!")
    
    def use_stat_point(self):
        """Распределить очки характеристик"""
        if self.stat_points <= 0:
            print("У вас нет очков для распределения!")
            return
        
        print("\nКуда хотите вложить очко характеристики?")
        print("1 - +10 HP")
        print("2 - +2 к атаке")
        print("3 - +2 к защите")
        print("4 - +2 к ловкости")
        print("0 - Отмена")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            self.hp_max += 10
            self.hp_current += 10
            print("HP увеличен на 10!")
        elif choice == "2":
            self.attack += 2
            print("Атака увеличена на 2!")
        elif choice == "3":
            self.defense += 2
            print("Защита увеличена на 2!")
        elif choice == "4":
            self.agility += 2
            print("Ловкость увеличена на 2!")
        elif choice == "0":
            return
        else:
            print("Неверный выбор!")
            return
        
        self.stat_points -= 1
        print(f"Осталось очков: {self.stat_points}")

# ==================== КЛАСС ПРЕДМЕТА ====================
class Item:
    @staticmethod
    def generate_random_item():
        """Создать случайный предмет"""
        item_types = [
            {"name": "Малое зелье здоровья", "type": "potion", "heal": 30, "price": 10},
            {"name": "Среднее зелье здоровья", "type": "potion", "heal": 50, "price": 20},
            {"name": "Ржавый меч", "type": "weapon", "attack_bonus": 2, "price": 30},
            {"name": "Стальной меч", "type": "weapon", "attack_bonus": 5, "price": 50},
            {"name": "Кожаный доспех", "type": "armor", "defense_bonus": 2, "price": 25},
            {"name": "Кольчуга", "type": "armor", "defense_bonus": 5, "price": 45},
            {"name": "Мешочек золота", "type": "gold", "amount": random.randint(10, 50), "price": 0}
        ]
        
        return random.choice(item_types)

# ==================== КЛАСС ВРАГА ====================
class Enemy:
    def __init__(self, floor):
        self.names = ["Гоблин", "Скелет", "Орк", "Тролль", "Зомби", "Волк"]
        self.name = random.choice(self.names)
        
        # Увеличиваем сложность с этажом
        multiplier = 1 + (floor - 1) * 0.3
        
        self.hp = random.randint(30, 60) * multiplier
        self.attack = random.randint(8, 15) * multiplier
        self.defense = random.randint(5, 10) * multiplier
        self.exp_reward = random.randint(20, 40) * multiplier
        self.coin_reward = random.randint(5, 20)
    
    def show_stats(self):
        """Показать характеристики врага"""
        print(f"\nПротивник: {self.name}")
        print(f"HP: {int(self.hp)} | Атака: {int(self.attack)} | Защита: {int(self.defense)}")
    
    def is_alive(self):
        """Проверить, жив ли враг"""
        return self.hp > 0

# ==================== ИГРОВОЙ МЕНЕДЖЕР ====================
class Game:
    def __init__(self):
        self.player = None
        self.current_floor = 1
        self.rooms_cleared = 0
        self.game_over = False
        self.next_rooms = {"left": None, "right": None}  # Для хранения реальных комнат
    
    def create_character(self):
        """Создание персонажа"""
        print("\n" + "="*50)
        print("СОЗДАНИЕ ПЕРСОНАЖА")
        print("="*50)
        print("Выберите расу:")
        print("1 - Человек (сбалансированный)")
        print("2 - Эльф (ловкий)")
        print("3 - Дворф (сильный и выносливый)")
        
        while True:
            choice = input("\nВаш выбор (1-3): ")
            
            if choice == "1":
                race = "Человек"
                break
            elif choice == "2":
                race = "Эльф"
                break
            elif choice == "3":
                race = "Дворф"
                break
            else:
                print("Пожалуйста, выберите 1, 2 или 3")
        
        self.player = Character(race)
        print(f"\nПерсонаж {race} создан!")
        self.player.show_stats()
    
    def show_inventory(self):
        """Показать инвентарь"""
        print("\n" + "="*50)
        print("ИНВЕНТАРЬ")
        print("="*50)
        
        if not self.player.inventory:
            print("Инвентарь пуст!")
            return
        
        for i, item in enumerate(self.player.inventory, 1):
            if item["type"] == "potion":
                print(f"{i}. {item['name']} (восстанавливает {item['heal']} HP)")
            elif item["type"] == "weapon":
                print(f"{i}. {item['name']} (+{item['attack_bonus']} к атаке)")
            elif item["type"] == "armor":
                print(f"{i}. {item['name']} (+{item['defense_bonus']} к защите)")
            elif item["type"] == "gold":
                print(f"{i}. {item['name']} ({item['amount']} золота)")
        
        print(f"\nЭкипировано:")
        if self.player.equipped_weapon:
            print(f"Оружие: {self.player.equipped_weapon['name']}")
        else:
            print("Оружие: нет")
        
        if self.player.equipped_armor:
            print(f"Броня: {self.player.equipped_armor['name']}")
        else:
            print("Броня: нет")
    
    def use_item(self):
        """Использовать предмет из инвентаря"""
        if not self.player.inventory:
            print("Инвентарь пуст!")
            return
        
        self.show_inventory()
        
        try:
            choice = int(input("\nВыберите номер предмета для использования (0 - отмена): "))
            if choice == 0:
                return
            
            item = self.player.inventory[choice - 1]
            
            if item["type"] == "potion":
                self.player.hp_current = min(self.player.hp_max, self.player.hp_current + item["heal"])
                print(f"Вы использовали {item['name']} и восстановили {item['heal']} HP!")
                self.player.inventory.pop(choice - 1)
            
            elif item["type"] == "weapon":
                if self.player.equipped_weapon:
                    print(f"Вы сняли {self.player.equipped_weapon['name']}")
                    self.player.inventory.append(self.player.equipped_weapon)
                
                self.player.equipped_weapon = item
                self.player.inventory.pop(choice - 1)
                print(f"Вы экипировали {item['name']}!")
            
            elif item["type"] == "armor":
                if self.player.equipped_armor:
                    print(f"Вы сняли {self.player.equipped_armor['name']}")
                    self.player.inventory.append(self.player.equipped_armor)
                
                self.player.equipped_armor = item
                self.player.inventory.pop(choice - 1)
                print(f"Вы экипировали {item['name']}!")
            
            elif item["type"] == "gold":
                self.player.coins += item["amount"]
                print(f"Вы получили {item['amount']} золота!")
                self.player.inventory.pop(choice - 1)
        
        except (ValueError, IndexError):
            print("Неверный выбор!")
    
    def drop_item(self):
        """Выбросить предмет из инвентаря"""
        if not self.player.inventory:
            print("Инвентарь пуст!")
            return
        
        self.show_inventory()
        
        try:
            choice = int(input("\nВыберите номер предмета для удаления (0 - отмена): "))
            if choice == 0:
                return
            
            item = self.player.inventory.pop(choice - 1)
            print(f"Вы выбросили {item['name']}")
        
        except (ValueError, IndexError):
            print("Неверный выбор!")
    
    def battle(self, enemy):
        """Бой с врагом"""
        print("\n" + "="*50)
        print(f"БОЙ С {enemy.name.upper()}!")
        print("="*50)
        
        while enemy.is_alive() and self.player.hp_current > 0:
            print(f"\nВаше HP: {self.player.hp_current}/{self.player.hp_max}")
            enemy.show_stats()
            
            print("\nВыберите действие:")
            print("1 - Атаковать")
            print("2 - Использовать предмет")
            print("3 - Попытаться уклониться")
            
            choice = input("Ваш выбор: ")
            
            if choice == "1":
                # Атака игрока
                player_damage = max(1, self.player.get_total_attack() - enemy.defense + random.randint(-2, 3))
                enemy.hp -= player_damage
                print(f"Вы нанесли {player_damage} урона!")
                
                # Проверка, выжил ли враг
                if not enemy.is_alive():
                    print(f"\nВы победили {enemy.name}!")
                    self.player.gain_exp(int(enemy.exp_reward))
                    self.player.coins += enemy.coin_reward
                    print(f"Получено {enemy.coin_reward} золота")
                    
                    # Шанс получить предмет
                    if random.random() < 0.3:
                        item = Item.generate_random_item()
                        self.player.inventory.append(item)
                        print(f"Получен предмет: {item['name']}")
                    
                    self.rooms_cleared += 1
                    break
                
                # Атака врага
                if self.player.hp_current > 0:
                    enemy_damage = max(1, enemy.attack - self.player.get_total_defense() + random.randint(-1, 2))
                    self.player.hp_current -= enemy_damage
                    print(f"{enemy.name} нанес вам {enemy_damage} урона!")
                    
                    if self.player.hp_current <= 0:
                        print("\nВы пали в бою...")
                        self.game_over = True
                        break
            
            elif choice == "2":
                self.use_item()
                
                # Враг атакует, если игрок использовал предмет
                if enemy.is_alive() and self.player.hp_current > 0:
                    enemy_damage = max(1, enemy.attack - self.player.get_total_defense() + random.randint(-1, 2))
                    self.player.hp_current -= enemy_damage
                    print(f"{enemy.name} нанес вам {enemy_damage} урона!")
            
            elif choice == "3":
                # Попытка уклониться
                dodge_chance = min(30, self.player.agility * 2)
                if random.randint(1, 100) <= dodge_chance:
                    print("Вы успешно уклонились от атаки!")
                else:
                    print("Уклонение не удалось!")
                    enemy_damage = max(1, enemy.attack - self.player.get_total_defense())
                    self.player.hp_current -= enemy_damage
                    print(f"{enemy.name} нанес вам {enemy_damage} урона!")
            else:
                print("Неверный выбор! Вы теряете ход.")
                
                # Враг атакует
                if enemy.is_alive() and self.player.hp_current > 0:
                    enemy_damage = max(1, enemy.attack - self.player.get_total_defense() + random.randint(-1, 2))
                    self.player.hp_current -= enemy_damage
                    print(f"{enemy.name} нанес вам {enemy_damage} урона!")
        
        print("\nБой окончен!")
    
    def generate_room_type(self):
        """Сгенерировать тип комнаты с весами"""
        room_types = ["enemy", "chest", "rest", "empty"]
        weights = [40, 25, 20, 15]
        return random.choices(room_types, weights=weights, k=1)[0]
    
    def get_room_name(self, room_type):
        """Получить читаемое название комнаты"""
        names = {
            "enemy": "Враг",
            "chest": "Сундук",
            "rest": "Отдых",
            "empty": "Пусто"
        }
        return names.get(room_type, "???")
    
    def generate_specific_room(self, room_type):
        """Генерация конкретной комнаты по типу"""
        print(f"\n{'='*50}")
        print(f"ЭТАЖ {self.current_floor} | КОМНАТА {self.rooms_cleared + 1}")
        print(f"{'='*50}")
        
        if room_type == "enemy":
            print("Вы встретили врага!")
            enemy = Enemy(self.current_floor)
            self.battle(enemy)
        
        elif room_type == "chest":
            print("Вы нашли сундук!")
            items_count = random.randint(1, 3)
            
            for i in range(items_count):
                item = Item.generate_random_item()
                self.player.inventory.append(item)
                
                if item["type"] == "gold":
                    print(f"Найдено: {item['name']} ({item['amount']} золота)")
                else:
                    print(f"Найдено: {item['name']}")
            
            self.rooms_cleared += 1
        
        elif room_type == "rest":
            print("Вы нашли комнату отдыха.")
            print("Здесь можно восстановить силы и потратить очки прокачки.")
            
            # Восстановление здоровья
            heal_amount = int(self.player.hp_max * 0.3)
            self.player.hp_current = min(self.player.hp_max, self.player.hp_current + heal_amount)
            print(f"Вы восстановили {heal_amount} HP")
            
            # Возможность потратить очки прокачки
            if self.player.stat_points > 0:
                use_points = input("\nХотите потратить очки характеристик? (да/нет): ").lower()
                if use_points == "да":
                    while self.player.stat_points > 0:
                        self.player.use_stat_point()
                        if self.player.stat_points > 0:
                            more = input("Потратить еще одно очко? (да/нет): ").lower()
                            if more != "да":
                                break
            
            self.rooms_cleared += 1
        
        elif room_type == "empty":
            print("Комната пуста...")
            self.rooms_cleared += 1
        
        # Проверка перехода на новый этаж
        if self.rooms_cleared >= 5:
            self.current_floor += 1
            self.rooms_cleared = 0
            print(f"\n Вы спустились на {self.current_floor} этаж! ")
            print("Враги стали сильнее...")
    
    def show_paths(self):
        """Показать пути и их содержимое"""
        print("\n" + "="*50)
        print("ВЫБОР ПУТИ")
        print("="*50)
        
        # Генерируем комнаты
        self.next_rooms["left"] = self.generate_room_type()
        self.next_rooms["right"] = self.generate_room_type()
        
        # Определяем видимость
        left_visible = random.random() < 0.6  
        right_visible = random.random() < 0.6
        
        print("\nПеред вами развилка:")
        
        if left_visible:
            left_name = self.get_room_name(self.next_rooms["left"])
            print(f"(1) Слева: {left_name}")
        else:
            print("(1) Слева: ???")
        
        if right_visible:
            right_name = self.get_room_name(self.next_rooms["right"])
            print(f"(2) Справа: {right_name}")
        else:
            print("(2) Справа: ???")
        
        print("(3) Посмотреть характеристики")
        print("(4) Открыть инвентарь")
        
        while True:
            choice = input("\nКуда пойти? (1-4): ")
            
            if choice == "1":
                self.generate_specific_room(self.next_rooms["left"])
                break
            elif choice == "2":
                self.generate_specific_room(self.next_rooms["right"])
                break
            elif choice == "3":
                self.player.show_stats()
            elif choice == "4":
                self.show_inventory_menu()
            else:
                print("Пожалуйста, выберите 1, 2, 3 или 4")
    
    def show_inventory_menu(self):
        """Показать меню инвентаря"""
        while True:
            print("\n" + "="*30)
            print("МЕНЮ ИНВЕНТАРЯ")
            print("="*30)
            print("1 - Просмотреть инвентарь")
            print("2 - Использовать предмет")
            print("3 - Выбросить предмет")
            print("0 - Вернуться")
            
            choice = input("Ваш выбор: ")
            
            if choice == "1":
                self.show_inventory()
            elif choice == "2":
                self.use_item()
            elif choice == "3":
                self.drop_item()
            elif choice == "0":
                break
            else:
                print("Неверный выбор!")
    
    def main_menu(self):
        """Главное меню игры"""
        print("\n" + "="*50)
        print("ТЕКСТОВАЯ RPG")
        print("="*50)
        print("1 - Начать новую игру")
        print("2 - Выйти")
        
        choice = input("\nВаш выбор: ")
        
        if choice == "1":
            self.create_character()
            self.play()
        elif choice == "2":
            print("До свидания!")
        else:
            print("Неверный выбор!")
            self.main_menu()
    
    def play(self):
        """Основной игровой цикл"""
        print("\n" + "="*50)
        print("ВЫ ВХОДИТЕ В ПОДЗЕМЕЛЬЕ...")
        print("="*50)
        
        while not self.game_over and self.player.hp_current > 0:
            self.show_paths()
            
            # Проверка на смерть
            if self.player.hp_current <= 0:
                print("\n" + "="*50)
                print("ИГРА ОКОНЧЕНА")
                print("="*50)
                print(f"Вы достигли {self.player.level} уровня")
                print(f"Вы прошли {self.current_floor} этажей")
                print(f"Собрано {self.player.coins} золота")
                break
            
            # Предложение сохраниться или выйти
            print("\n" + "-"*30)
            print("1 - Продолжить исследование")
            print("2 - Посмотреть характеристики")
            print("3 - Открыть инвентарь")
            print("4 - Выйти в главное меню")
            
            choice = input("Ваш выбор: ")
            
            if choice == "2":
                self.player.show_stats()
            elif choice == "3":
                self.show_inventory_menu()
            elif choice == "4":
                print("Возвращаемся в главное меню...")
                self.main_menu()
                break
        
        if self.player.hp_current <= 0:
            input("\nНажмите Enter для возврата в главное меню...")
            self.main_menu()

# ЗАПУСК ИГРЫ
if __name__ == "__main__":
    print("Добро пожаловать в ТЕКСТОВУЮ RPG!")
    game = Game()
    game.main_menu()