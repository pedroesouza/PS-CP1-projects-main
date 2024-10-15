#Pedro Souza, Authorized
authorized = ["Pedro", "Not Jackson", "Boe Jiden", "Kendrick Lamar", "Potato Enjoyer 3", "The Guy From Amongus", "IDK", "Olaf From Frozen", "Justin Beiber"]
admins = ["Pedro", "Justin Bieber", "Boe Jiden"]
user = input("Who are you?: ")

if user in authorized:
    if user in admins:
        print("Hello admin, welcome to the crappy python project that you for some reason are an admin for.")
    else:
        print("You are authorized in... well... the... whatever this is.")
elif user not in authorized:
    print("You're not allowed, GET OUT!?!?!?!?!?! 😠🤬😠😡😠👹😠👺😠💢💢💢")

