# 22.04.23
import random
import time


class Player:
    def __init__(self,name,rasse,profess):
        self.name = name
        self.hp=self.create_hero(rasse,profess)[0]
        self.damage = self.create_hero(rasse,profess)[1]
        self.lavel = 1
        self.rass = rasse
        self.prof = profess
        self.xp = 0
    def attack (self,target):
        target.hp -= self.damage
        print(f"Вы нанесли урон и у врага осталось {target.hp} здоровья")
        if target.hp <= 0:
            print("Вы победили врага")
            self.xp += 10
            if self.xp >= 50:
                self.lavel += 1
                self.hp += 20
                self.damage += 20
                self.xp = 0
                print(f"У вас {self.lavel} уровень")

    def create_hero(self,rasse,you_profession):
        hp=0
        damage=0
        if rasse == "human":
            hp += 50
            damage += 10
        elif rasse == "elf":
            hp += 120
            damage += 50
        elif rasse == "dworf":
            hp += 1000
            damage += 120

        if you_profession == "archer":
            hp += 30
            damage += 150
        elif you_profession == "warrior":
            hp += 200
            damage += 100
        elif you_profession == "knight":
            hp += 96
            damage += 112
        return(hp,damage)
class Enemy:
    def __init__(self,name,player):
        self.name = name
        self.hp = self.create_enemy(player.lavel)[0]
        self.damage = self.create_enemy(player.lavel)[1]
    def create_enemy(self,lavel):
        hp = random.randint(35,60)*lavel
        damage = random.randint(10,30)*lavel
        return(hp,damage)
    def attack_people(self,hum):
        hum.hp -= self.damage
        print(f"Вам нанесли урон, у вас осталось {hum.hp} здоровья")
        if hum.hp <= 0:
            print("Вы проиграли")
            quit()

per = input("Введите имя героя: ")
m = ["human","elf","dworf"]
profession = ["archer","warrior","knight"]
print("Доступные расы: ",*m)
rasse = input(f"К какой расе ты пренадлежишь? ")
mob = ["zomdi","skilet","kriper"]
print("Доступные профессии: ",*profession)
you_profession = input(f"Какую профессию ты выберешь? ")
exempt = Player(per,rasse,you_profession)

# Хлеб - bread 25% + 5 xp
# Картошка - potato 15 % + 10 xp
# меч - sword 10% + 35 damage
# сердце - heart 30% + 20xp
# vila 20% + 20 damage



while True:
    r = random.randint(1,10)
    if r <= 6:
        mob=Enemy(player=exempt,name="Вася")
        while mob.hp > 0:
            exempt.attack(mob)
            if mob.hp > 0:
                mob.attack_people(exempt)
        print()
        time.sleep(2)
    else:
        chance = random.randint(1,100)
        if chance < 25:
            print("вы нашли ХЛЕБ")
            exempt.hp += 5
        elif chance >25 and chance <= 40:
            print("вы нашли КАРТОШКУ")
            exempt.hp += 10
        elif chance > 40 and chance <=50:
            print("вы нашли МЕЧ")
            exempt.damage += 20
        elif chance >50 and chance <= 80:
            print("вы нашли СЕРДЦЕ")
            exempt.hp += 20
        elif chance >80:
            print("вы нашли ВИЛЫ")
            exempt.damage += 10

