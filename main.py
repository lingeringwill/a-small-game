import random


def main():
    enemy_hp: float = 10.0

    player_hp: float = 10.0

    attack_delta_hp: int = 1

    while True:
        player_input = input("please press a or d to attack or defend")

        if player_input == 'a':
            player_hp -= attack_delta_hp

            if random.choice([True, False]):
                enemy_hp -= (2*attack_delta_hp)

            else:
                enemy_hp -= attack_delta_hp

        else:

            if random.choice([True, False]):
                player_hp -= (attack_delta_hp/2)

        if enemy_hp <= 0 and player_hp <= 0:
            print("It's a draw")

            return
        elif enemy_hp <= 0:
            print("you won!")

            return
        elif player_hp <= 0:
            print("bruh, the enemy won")

            return
        else:
            f"enemy_hp: {enemy_hp} player_hp: {player_hp}"

            print(f"enemy_hp: {enemy_hp} player_hp: {player_hp}")



        

main()