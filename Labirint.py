import random

class Profession: #Класс профессий гг
    def __init__(self, hp_boost: int, mana_boost: int, manaregen_boost: int, physical_boost: int, magical_boost: int, accuracy_boost: int ): #Параметры профессий героя:
        self.hp_boost = hp_boost #Доп ОЗ
        self.mana_boost = mana_boost #Доп мана
        self.manaregen_boost = manaregen_boost #Доп реген маны
        self.physical_boost = physical_boost #Доп физ атака
        self.magical_boost = magical_boost #Доп маг сила
        self.accuracy_boost = accuracy_boost #Доп точность
Swordsman = Profession(20, 30, 5, 80, 0, 0) 
Magician = Profession(0, 100, 15, 0, 100, 0) 
Archer = Profession(5, 50, 10, 10, 5, 20)
def Swordsman_skills(mana: int, physical_skills: int, enemy_resistance: int):
    damage = 0
    print("Available skills:\n1)<Base sword attack>(Mana costs: 0, Damage: 80% physical skills)\n\
2)<28 sword strikes>: Performs incredibly fast sword strikes (Mana costs: 10, Damage: 120% physical skills).\n\
3)<The Flaming God of Thunder>: The hero makes a huge leap towards the enemy, cutting him down with his sword(Mana costs: 20, Damage: 260% physical skills).")
    print("Choose the skill you want to use:")
    while damage == 0:
        ch=int(input())
        if ch == 1:
            damage = int(physical_skills*0.8) - enemy_resistance
        elif ch == 2:
            if mana>=10:
                damage = int(physical_skills * 1.2) - enemy_resistance
                mana-=10
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        elif ch == 3:
            if mana>=20:
                damage = int(physical_skills * 2.6) - enemy_resistance
                mana-=20
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        mana+=manaregen
    return [mana,damage]
def Magician_skills(mana: int, magical_skills: int, enemy_resistance: int):
    damage = 0
    print("Available skills:\n\
1)<Infinity: Blue>: Creates a small black hole with a strong gravitational \
pull and sends it towards enemies. Due to gravity, enemies are pulled towards a single point.(Mana costs: 0, Damage: 60% magical skills)\n\
2)<Infinity reversed technique: Red>: Creates the opposite of <Blue> - a mana clot that repels everything in its path.(Mana costs: 20, Damage: 180% magical skills)\n\
3)<Hollow Technique: Purple>: Combines the pull of Blue and the Push of red into one sphere. This creates a powerful imaginary mass that \n\
obliterates anything in its path.(Mana costs: 40, Damage: 400% magical skills)\n\
4)<Domain expansion: Unlimited Void>: Creates a space that sends all kinds of stimuli and information into opponent's brain practically short-circuiting them.\
(Mana costs: 50, Damage: 600% magical skills)") 
    print("Choose the skill you want to use:")
    while damage == 0:
        ch = int(input())
        if ch == 1:
            damage = int((magical_skills * 0.6)) - enemy_resistance
        elif ch == 2:
            if mana >= 20:
                damage = int((magical_skills * 1.8)) - enemy_resistance
                mana-=20
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        elif ch == 3:
            if mana >= 40:
                damage = int((magical_skills * 4)) - enemy_resistance
                mana-=40
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        elif ch == 4:
            if mana >= 50:
                damage = int((magical_skills * 6)) - enemy_resistance
                mana-=50
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        mana+=manaregen
    return [mana,damage]
def Archer_skills(mana: int, physical_skills: int, magical_skills: int, accuracy: int):
    damage = 0
    print("ALL ARCHER SKILLS IGNORE ENEMY RESISTANCE!!!")
    print("Available skills:\n\
1)<Basic Archery>: Shoots an arrow from a bow that is not charged with mana.(Mana costs: 0, Damage: 40% physical skills +  100% accuracy)\n\
2)<Fire arrow>: Shoots an arrow charged with fire mana.(Mana costs: 15, Damage: 60% physical skills + 60% magical skills + 100% accuracy)\n\
3)<The lightning Arrow>: Shoots an arrow charged with lightning mana.(Mana costs: 30, Damage: 100% physical skills + 100% magical skills +100% accuracy)")
    print("Choose the skill you want to use:")
    while damage == 0:
        ch = int(input())
        if ch == 1:
                damage = int((physical_skills * 0.4 + accuracy * 1))
        elif ch == 2:
            if mana >= 15:
                damage = int((physical_skills* 0.6 + magical_skills * 0.6 + accuracy * 1))
                mana-=15
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        elif ch == 3:
            if mana >= 30:
                damage = int((physical_skills * 1 + magical_skills * 1 + accuracy * 1))
                mana-=30
            else:
                print("You don't have enough mana to use this skill. Choose another one:")
        mana+=manaregen
    return [mana,damage]
professions = ['Swordsman', 'Archer', 'Magician']
class Monsters: #Класс монстров
    def __init__(self, hp: int, attack: int, resistance: str): #Параметры монстров
        self.hp = hp #ОЗ
        self.attack = attack #Атака
        self.resistance = resistance #Устойчивость к типам урона
Ghoul = Monsters(50, 20, 'Physical')
Ogre = Monsters(150, 10, 'Magical')
Demon = Monsters(100, 20, 'All')
Monsters_list = ['Ghoul', 'Ogre', 'Demon']
def chest_res(backpack: list):
    item = random.choice(items)
    backpack.append(item)
    print(f'You found the {item}! You have {backpack.count(item)} {item} ')
    if item  == 'Healing potion':
        print('Healing potion: You can restore 20HP.')
    elif item == 'Power Up':
        print('Power Up: Gives +5 to the maximum value of all attributes.')
    elif item == 'Poison':
        print("Poison: -20 to the enemy's HP.")
    elif item == 'Change of profession':
        print('Change of profession: You can change your profeccion (Swordsman, Archer, Magician)')
    return backpack
def Monster(hp: int, mana: int, physical_skills: int, magical_skills: int, accuracy: int, profession: str, backpack: list):
    monster = random.choice(Monsters_list)
    if monster == 'Ghoul':
        monster_hp = Ghoul.hp 
        monster_attack = Ghoul.attack
        monster_phys_resist = 10
        monster_magic_resist = 0
        print("You've met a Ghoul!")
    if monster == 'Ogre':
        monster_hp = Ogre.hp 
        monster_attack = Ogre.attack
        monster_phys_resist = 0
        monster_magic_resist = 10
        print("You've met an Ogre!")
    if monster == 'Demon':
        monster_hp = Demon.hp 
        monster_attack = Demon.attack
        monster_phys_resist = 10
        monster_magic_resist = 10
        print("You've met a Demon!")
    print(f'Enemy hp: {monster_hp}')
    print(f'Enemy attack: {monster_attack}')
    print(f'Enemy physical resistance: {monster_phys_resist}')
    print(f'Enemy magical resistance: {monster_magic_resist}')
    if 'Poison' in backpack:
        print(' ')
        print('Do you want to use poison before fight?(Y/N)')
        ans = str(input())
        if ans == 'Y':
            backpack = backpack.pop(backpack.index('Poison'))
            monster_hp-=20
    print(' ')
    while (monster_hp > 0) and (hp >0):
            print(f'Enemy hp: {monster_hp}')
            print(f'Enemy attack: {monster_attack}')
            print(f'Enemy physical resistance: {monster_phys_resist}')
            print(f'Enemy magical resistance: {monster_magic_resist}')
            print(' ')
            print(f'Your hp: {hp}')
            print(f'Your mana: {mana}')
            print(f'Your Physical skills: {physical_skills}')
            print(f'Your Magical skills: {magical_skills}')
            mana_end = 0
            damage = 0
            if profession == 'Swordsman':
                fight_res = Swordsman_skills(mana, physical_skills, monster_phys_resist)
                mana_end = fight_res[0]
                damage = fight_res[1]
            elif profession == 'Magician':
                fight_res = Magician_skills(mana, magical_skills, monster_magic_resist)
                mana_end = fight_res[0]
                damage = fight_res[1]
            elif profession == 'Archer':
                fight_res = Archer_skills(mana, physical_skills, magical_skills, accuracy)
                mana_end = fight_res[0]
                damage = fight_res[1]
            mana = mana_end
            monster_hp -= damage
            if monster_hp <= 0:
                break
            else:
                hp -= monster_attack
    return [monster_hp, hp, mana, backpack]
def Key(backpack: list):
    print("You've found a key. Now you can open the portal.")
    backpack.append('Key')
    return backpack
def Trap(hp: int):
    print("You enter a room with a trap and lose 10 HP")
    return hp-10
def Portal(backpack: list):
    if 'Key' in backpack:
        print("You've found the portal! Now you can live the dungeon!")
        return 1
    else:
        print("You've found the portal! Unfortunately, you don't have a key, so find one and return to this room.")
        return 0
def Healing_potion(hp: int, backpack: list):
    if 'Healing potion' in backpack:
        print('Your HP has been restored!')
        backpack.pop(backpack.index('Healing potion'))
        return [hp+20, backpack]
    else:
        print("You have no Healing potion in your backpack.")
        return [hp,backpack]
def Change_of_profession(backpack: list, hp: int, max_mana: int, manaregen: int, physical_skills: int, magical_skills: int, accuracy: int, profession: str):
    if 'Change of profession' in backpack:
        if profession == 'Swordsman':
            hp=max(1, hp -Swordsman.hp_boost)
            max_mana-=Swordsman.mana_boost
            manaregen-=Swordsman.manaregen_boost
            physical_skills-=Swordsman.physical_boost
        elif profession == 'Magician':
            max_mana-=Magician.mana_boost
            manaregen-=Magician.manaregen_boost
            magical_skills-=Magician.magical_boost
        elif profession == 'Archer':
            hp=max(1, hp-Archer.hp_boost)
            max_mana-=Archer.mana_boost
            manaregen-=Archer.manaregen_boost
            physical_skills-=Archer.physical_boost
            magical_skills-=Archer.magical_boost
            accuracy-=Archer.accuracy_boost
        print("Which profession would you like to have?(1.Swordsman, 2.Magician, 3.Archer)(1/2/3)")
        backpack.pop(backpack.index('Change of profession'))
        ch = int(input())
        if ch == 1:
            print("Now you are a Swordsman")
            return ['Swordsman', backpack, hp, max_mana, manaregen, physical_skills, magical_skills, accuracy]
        elif ch == 2:
            print("Now you are a Magician")
            return ['Magician', backpack, hp, max_mana, manaregen, physical_skills, magical_skills, accuracy]
        else:
            print("Now you are an Archer")
            return ['Archer', backpack, hp, max_mana, manaregen, physical_skills, magical_skills, accuracy]
    else:
        print("You have no Change of profession in your backpack.")
def backpack_inside(backpack: list):
    print(f'You have:\n\
1)Healing potion: {backpack.count('Healing potion')};\n\
2)Power Up: {backpack.count('Power Up')};\n\
3)Poison: {backpack.count('Poison')};\n\
4)Change of profession: {backpack.count('Change of profession')};\n\
5)Key: {backpack.count('Key')}.')
rooms =  ['E', 'C', 'M', 'K', 'T'] # E - Empty room; C - Chest with items; M - Monster; K - Key; T - Trap
items = ['Healing potion', 'Power Up', 'Poison', 'Change of profession']
print('What size of labyrinth do you want to create? (Enter n,m)')
n,m = map(int, input().split())
labyrinth = [[random.choice(rooms) for i in range(n)] for j in range(m)]
x = 1
y = 1
hp = 100 
max_mana = 100
mana = 10
manaregen = 10
physical_skills = 10
magical_skills = 10
accuracy = 10 
profession = random.choice(professions)
backpack = []
labyrinth[m-1][n-1] = 'P'
labyrinth[0][0] = 'E'
lab_interface = [['*' for x in range(n)] for i in range(m)]
lab_interface[0][0] = 'X'
print("Basic stats:")
print(f'HP: {hp}')
print(f'Mana: {mana}')
print(f'Max mana: {max_mana}')
print(f'Manaregen: {manaregen}')
print(f'Physical skills: {physical_skills}')
print(f'Magical skills: {magical_skills}')
print(f'Accuracy: {accuracy}')
print("Your first profession was chosen by chance. You are " + profession)
print("Each profession gives its own bonuses.")
print("1.Swordsman:\n\
    1)HP: +20;\n\
    2)Max mana: +30\n\
    3)Manaregen: +5;\n\
    4)Physical skills: +80.")
print("2.Magician:\n\
    1)Max mana: +100;\n\
    2)Manaregen: +15;\n\
    3)Magical skills: +100.")
print("3.Archer\n\
    1)HP: +5;\n\
    2)Max mana: +50;\n\
    3)Manaregen: +10;\n\
    4)Physical skills: +10;\n\
    5)Magical skills: +5;\n\
    6)Accuracy: +20.")
print("You can start the game now. Good luck!")
print("Controllers:\n\
1) w - go up;\n\
2) s - go down;\n\
3) a - go left;\n\
4) d - go right;\n\
5) stats - shows your characteristics;\n\
6) backpack - shows your inventory;\n\
7) heal - use a Healing potion if there is one;\n\
8) PowerUp - use Power Up if there is one;\n\
9) ChangeProf - нou can change your profession if you have the necessary item.")
if profession == 'Swordsman':
    hp+=Swordsman.hp_boost
    max_mana+=Swordsman.mana_boost
    manaregen+=Swordsman.manaregen_boost
    physical_skills+=Swordsman.physical_boost
elif profession == 'Magician':
    max_mana+=Magician.mana_boost
    manaregen+=Magician.manaregen_boost
    magical_skills+=Magician.magical_boost
elif profession == 'Archer':
    hp+=Archer.hp_boost
    max_mana+=Archer.mana_boost
    manaregen+=Archer.manaregen_boost
    physical_skills+=Archer.physical_boost
    magical_skills+=Archer.magical_boost
    accuracy+=Archer.accuracy_boost
while hp > 0:
    for i in range(m):
        print(lab_interface[i])
    print(' ')
    print('X - your location;')
    print("E - an empty room that you've already visited;")
    print("* - unknown rooms.")
    print('Enter the command:')
    fl = 0
    lab_interface[y-1][x-1] = 'E'
    com = str(input())
    if com == 'w':
        if (y-1 <= 0):
            print("You can't go up. Please choose another command.")
        else:
            y-=1
            fl = 1
    if com == 's':
        if (y+1 > m):
            print("You can't go down. Please choose another command.")
        else:
            y+=1
            fl = 1
    if com == 'a':
        if (x-1 <= 0):
            print("You can't go left. Please choose another command.")
        else:
            x-=1
            fl = 1
    if com == 'd':
        if (x+1 > n):
            print("You can't go right. Please choose another command.")
        else:
            x+=1
            fl = 1
    room = labyrinth[y-1][x-1]
    lab_interface[y-1][x-1] = 'X'
    if fl == 1:
        if room == 'E':
            print('There is nothing in  this room')
            mana=min(max_mana, manaregen + mana)
        elif room == 'C':
            backpack = chest_res(backpack)
            mana=min(max_mana, manaregen + mana)
        elif room == 'M':
            res_fight = Monster(hp, mana, physical_skills, magical_skills, accuracy, profession, backpack)
            hp_monster = res_fight[0]
            hp = res_fight[1]
            mana = res_fight[2]
            backpack = res_fight[3]
            if hp<=0:
                print('You lose!')
                break
            else:
                print("You've defeated the monster! Congratulations!")
        elif room == 'K':
            backpack = Key(backpack)
            mana=min(max_mana, manaregen + mana)
        elif room == 'T':
            hp=Trap(hp)
            mana=min(max_mana, manaregen + mana)
        elif room == 'P':
            k = Portal(backpack)
            if k == 1:
                print("You've passed the dungeon. Congratulations, bro!")
                break
    if com == 'stats':
        print(f'Your hp: {hp}')
        print(f'Your mana: {mana}')
        print(f'Your manaregen: {manaregen}')
        print(f'Your MAX mana: {max_mana}')
        print(f'Your Physical skills: {physical_skills}')
        print(f'Your Magical skills: {magical_skills}')
        print(f'Your Accuracy: {accuracy}')
    if com == 'backpack':
        backpack_inside(backpack)
    if com == 'heal':
        heal_res = Healing_potion(hp, backpack)
        hp = heal_res[0]
        backpack = heal_res[1]
    if com == 'PowerUp':
        if 'Power Up' in backpack:
            print('Your stats were increased')
            hp+=5
            max_mana+=5
            mana+=5
            manaregen+=5
            physical_skills+=5
            magical_skills+=5
            accuracy+=5
            backpack.pop(backpack.index('Power Up'))
        else:
            print("You have no Power Up in your backpack")
    if com == 'ChangeProf':
        prof_res = Change_of_profession(backpack, hp, max_mana, manaregen, physical_skills, magical_skills, accuracy, profession)
        profession = prof_res[0]
        backpack = prof_res[1]
        hp = prof_res[2]
        max_mana = prof_res[3]
        manaregen = prof_res[4]
        physical_skills = prof_res[5]
        magical_skills = prof_res[6]
        accuracy = prof_res[7]
        if profession == 'Swordsman':
            hp+=Swordsman.hp_boost
            max_mana+=Swordsman.mana_boost
            manaregen+=Swordsman.manaregen_boost
            physical_skills+=Swordsman.physical_boost
        elif profession == 'Magician':
            max_mana+=Magician.mana_boost
            manaregen+=Magician.manaregen_boost
            magical_skills+=Magician.magical_boost
        elif profession == 'Archer':
            hp+=Archer.hp_boost
            max_mana+=Archer.mana_boost
            manaregen+=Archer.manaregen_boost
            physical_skills+=Archer.physical_boost
            magical_skills+=Archer.magical_boost
            accuracy+=Archer.accuracy_boost
    
