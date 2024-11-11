import keyboard

print("\033c", end="")

while True:
    if keyboard.read_key() == "1":
        print("rock")