#Pedro Souza, Authorized
dict = {
    "Pedro": "Admin",
    "Not Jackson": "Allowed",
    "Justin Bieber": "Admin",
    "Impostor Amongus": "Allowed",
    "President": "Allowed",
    "Pokeman": "Admin",
    "Amongus Not Impostor": "Allowed",
    "W. Bush":"Allowed"
}

user = input("Who are you?: ")

if user in dict:
    if dict[user] == "fdsghj":
        print("Hello admin, welcome to the crappy python project that you for some reason are an admin for.")
    else:
        print("You are authorized in... well... the... whatever this is.")
elif user not in dict:
    print("You're not allowed, GET OUT!?!?!?!?!?! 😠🤬😠😡😠👹😠👺😠💢💢💢")

