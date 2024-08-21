def interface_intro():
    print("Welcome to the Tic Tac Toe game!")
    print("-------------------")
    print("Write coordinates to place your symbol in x y format!")
    print("-------------------")
    print("Press Enter to start your game!")
    input()


interface_intro()

print("-------------------")
player1_name = str(input("Write Player 1 name:"))
player2_name = str(input("Write Player 2 name:"))
print("Press Enter to continue")
input()

level = [[" "] * 3 for i in range(3)]


def level_structure_top():
    print("That`s your board:")
    print()
    print(f" y/x| 0 | 1 | 2 | ")
    print("  --------------- ")


def level_structure_body():
    for i, row in enumerate(level):
        row = f"  {i} | {' | '.join(row)} | "
        print(row)
        print("  --------------- ")
    print()


def ask_Player(player_name):
    while True:
        x, y = map(int, input(f" Your decision {player_name}: ").split())

        if (x < 0 or x > 2) or (y < 0 or y > 2):
            print(" Write coordinates between 0 and 2 ")
            continue

        if level[x][y] != " ":
           print(" This spot is taken ")
           continue
        break
    return x, y

def win_condition():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cordinates in win_cord:
        symbols = []
        for c in cordinates:
            symbols.append(level[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(f" {player1_name} WON!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print(f" {player2_name} WON!!!")
            return True
    return False


# %%

level = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    level_structure_top()
    level_structure_body()
    print(count)
    if count % 2 == 1:
        print(f" {player1_name} it`s your turn ")
        x, y = ask_Player(player1_name)
        level[x][y] = "X"
    else:
        print(f" {player2_name} it`s your turn")
        x, y = ask_Player(player2_name)
        level[x][y] = "0"


    if win_condition():
        level_structure_top()
        level_structure_body()
        break

    if count == 9:
        print(" It`s a tie!")
        break
