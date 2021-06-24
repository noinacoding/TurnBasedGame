import random
import time


# Easy Enemy Stats
def enemy_health():
    return random.randint(80, 300)


def enemy_atk():
    return random.randint(8, 30)


def enemy_protection():
    return random.randint(3, 5)


# Warrior Stats
def player_attack():
    return random.randint(10, 20)


def player_protection():
    return random.randint(4, 6)


def player_hp():
    return random.randint(150, 180)


# Pick mode, class, start game

def pickclass():
    mode = str(input("Please pick enemy difficulty (Easy) (Default) "))
    if mode == "Easy":
        print("Currently class is [Warrior]")
        job = str(input("Please pick your class "))
        if job == "Warrior":
            print("----------[Loading..]----------")
            time.sleep(3)
            print("----------[Starting..]----------")
            time.sleep(2)
            player_turn(attack, protect, enemy_attack, enemy_protect, enemy_hp, hp, job, enemy_class)
        else:
            print("Invalid class please pick again")
            print("--------------------")
            pickclass()
    else:
        print("Invalid mode please pick again")
        pickclass()


# Easy Mode
enemy_hp = enemy_health()
enemy_attack = enemy_atk()
enemy_protect = enemy_protection()
enemy_class = "Warrior"

# Class Warrior
hp = player_hp()
attack = player_attack()
protect = player_protection()


# Warrior Skill
def attack_rose():
    return random.randint(3, 7)


def defense_rose():
    return random.randint(1, 2)


# Easy Enemy Warrior Skill
def enemy_attack_rose():
    return random.randint(3, 5)


def enemy_defense_rose():
    return random.randint(1, 2)


def player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick, ea_class):
    def win(hitp, bot_hitp):
        if ea_class == "Warrior":
            if hitp >= 1 and bot_hitp <= 0:
                time.sleep(1)
                print("WHAT?! The enemy seems knock out? is that mean..")
                time.sleep(1)
                print("YOU WONNNNN")
            elif hitp <= 0 and bot_hitp >= 1:
                time.sleep(1)
                print("LMAO WHAT DA FAQ YOU DED LOLOLOL")
            else:
                print("----------[Bot turn]-----------")
                random_attack_warrior(ea_input, enemy_protect, hitpoint, protect_input, attack_input)

    def winbot(hitp, bot_hitp):
        if hitp >= 1 and bot_hitp <= 0:
            time.sleep(1)
            print("WHAT?! The enemy seems knock out? is that mean..")
            time.sleep(1)
            print("YOU WONNNNN")
        elif hitp <= 0 and bot_hitp >= 1:
            time.sleep(1)
            print("LMAO WHAT DA FAQ YOU DED LOLOLOL")
        else:
            print("----------[Player turn]-----------")
            player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitp, classpick, ea_class)

    if ea_class == "Warrior":
        def random_attack_warrior(input_enemy_attack, input_enemy_defense, playerhitpoint, playerdefense, playerattack):
            generate = random.randint(1, 5)
            if generate == 1:
                time.sleep(3)
                print("Enemy pick his sword up and sharpen it in front of you menacingly..")
                time.sleep(2)
                input_enemy_attack += enemy_attack_rose()
                print("Enemy damage is now increased")
                print("----------[Player turn]----------")
                player_turn(attack_input, protect_input, input_enemy_attack, input_enemy_defense, enemy_hitpoint,
                            hitpoint,
                            classpick, ea_class)
            elif generate == 2:
                if input_enemy_defense >= playerattack - 1:
                    time.sleep(3)
                    print("Enemy slash toward you with strength and speed")
                    playerhitpoint -= input_enemy_attack
                    time.sleep(2)
                    playerhitpoint += playerdefense
                    print("Kapow you take", input_enemy_attack, "damage and some of it have blocked by your shield")
                    winbot(playerhitpoint, enemy_hitpoint)
                else:
                    time.sleep(3)
                    print("Enemy somehow cleaning his shield and you can't attack him while that wtf")
                    time.sleep(2)
                    input_enemy_defense += enemy_defense_rose()
                    print("Enemy defense is now increased")
                    print("----------[Player turn]----------")
                    player_turn(attack_input, protect_input, input_enemy_attack, input_enemy_defense, enemy_hitpoint,
                                hitpoint, classpick, ea_class)
            elif generate >= 3:
                time.sleep(3)
                attack_patterns_bot = random.randint(1, 10)
                if attack_patterns_bot <= 5:
                    print("Enemy slash toward you with strength and speed")
                    playerhitpoint -= input_enemy_attack
                    time.sleep(2)
                    playerhitpoint += playerdefense
                    print("Kapow you take", input_enemy_attack, "damage and some of it have blocked by your shield")
                    winbot(playerhitpoint, enemy_hitpoint)
                elif attack_patterns_bot == 6 or attack_patterns_bot == 7:
                    print("Enemy slash toward you with strength and speed")
                    time.sleep(2)
                    print("!! Enemy gain strength and speed due to position in fight which give him critical damage")
                    playerhitpoint -= input_enemy_attack + 2
                    time.sleep(2)
                    playerhitpoint += playerdefense / 2
                    print("Kapow you take", input_enemy_attack + 2, "damage and you can't block most of the damage")
                    winbot(playerhitpoint, enemy_hitpoint)
                elif attack_patterns_bot == 8 or attack_patterns_bot == 9:
                    print("Enemy slash toward you with strength and speed")
                    playerhitpoint -= input_enemy_attack / 2
                    time.sleep(2)
                    print("!! You dodge enemy slash but enemy attack you again and deal less damage to you")
                    playerhitpoint += playerdefense
                    print("Kapow you take", input_enemy_attack / 2, "damage and some of it have blocked by your shield")
                    winbot(playerhitpoint, enemy_hitpoint)
                elif attack_patterns_bot == 10:
                    print("Enemy slash toward you with strength and speed")
                    time.sleep(2)
                    print("!! You predict enemy move and dodge which make enemy fully miss to attack")
                    winbot(playerhitpoint, enemy_hitpoint)

    choice = str(input("Please pick your choice between Moves ,Inspect, Self Inspect "))

    if choice == "Inspect":
        print("You look at the enemy and get some of the info..")
        time.sleep(2)
        print("Enemy name is unknown")
        print("Enemy class is ", ea_class)
        print("Enemy health is", int(enemy_hitpoint))
        print("Enemy damage is around", ea_input)
        print("Enemy defense is", ep_input)
        time.sleep(2)
        print("----------[Player turn]----------")
        player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                    ea_class)

    elif choice == "Self Inspect":
        print("You look at yourself and estimate your power")
        time.sleep(2)
        print("Your name is", name)
        print("Your class is", classpick)
        print("Your health is", int(hitpoint))
        print("Your damage is around", attack_input)
        print("Your defense is", protect_input)
        time.sleep(2)
        print("----------[Player turn]----------")
        player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                    ea_class)

    if choice == "Moves":
        if classpick == "Warrior":
            move_choice = str(input("Please pick between Sword sharpen, Shield clean, Slash, or Go back "))
            if move_choice == "Sword sharpen":
                print("You pick your sword up and sharpen it in front of the enemy menacingly..")
                time.sleep(2)
                attack_input += attack_rose()
                print("Your damage is now increased")
                print("----------[Bot turn]-----------")
                random_attack_warrior(ea_input, enemy_protect, hitpoint, protect_input, attack_input)

            elif move_choice == "Shield clean":
                print("You somehow cleaning your shield in the middle of the battle..")
                time.sleep(2)
                if protect_input >= ea_input - 1:
                    print("You currently max your defense stat for now")
                    print("----------[Player turn]-----------")
                    player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                                ea_class)
                else:
                    protect_input += defense_rose()
                    print("Your defense is now increased")
                    print("----------[Bot turn]-----------")
                    random_attack_warrior(ea_input, enemy_protect, hitpoint, protect_input, attack_input)

            elif move_choice == "Slash":
                attack_patterns = random.randint(1, 10)
                if attack_patterns <= 5:
                    print("You slash toward your enemy with strength and speed")
                    enemy_hitpoint -= attack_input
                    time.sleep(2)
                    enemy_hitpoint += ep_input
                    print("Result in sight! You deal", attack_input,
                          "damage to enemy and some of your damage is blocked")
                    win(hitpoint, enemy_hitpoint)
                elif attack_patterns == 6 or attack_patterns == 7:
                    print("You slash toward your enemy with strength and speed")
                    time.sleep(2)
                    print("!! You gain strength and speed due to position in fight which give you critical damage")
                    enemy_hitpoint -= attack_input + 2
                    time.sleep(2)
                    enemy_hitpoint += ep_input / 2
                    print("Result in sight! You deal", attack_input + 2,
                          "damage to enemy and most of the damage can't be "
                          "blocked")
                    win(hitpoint, enemy_hitpoint)
                elif attack_patterns == 8 or attack_patterns == 9:
                    print("You slash toward your enemy with strength and speed")
                    time.sleep(2)
                    print("!! Enemy dodge your slash but you attack him again and deal less damage than usual")
                    enemy_hitpoint -= attack_input / 2
                    time.sleep(2)
                    enemy_hitpoint += ep_input
                    print("Result in sight! You deal", attack_input / 2,
                          "damage to enemy and some of your damage is blocked")
                    win(hitpoint, enemy_hitpoint)
                elif attack_patterns == 10:
                    print("You slash toward your enemy with strength and speed")
                    time.sleep(2)
                    print("!! Enemy predict your move and dodge which make you fully miss to attack")
                    win(hitpoint, enemy_hitpoint)

            elif move_choice == "Go back":
                player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                            ea_class)
            else:
                print("Your input is not in any option maybe you spell it wrong")
                player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                            ea_class)

    else:
        if enemy_hitpoint > 0 and hitpoint > 0:
            print("Your input is not in any option maybe you spell it wrong")
            player_turn(attack_input, protect_input, ea_input, ep_input, enemy_hitpoint, hitpoint, classpick,
                        ea_class)
        else:
            print("----------[Thanks for playing]----------")


# Start game
name = str(input("Please enter your hero name "))
pickclass()
