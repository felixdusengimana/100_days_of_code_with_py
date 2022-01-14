from player import Player

player1 = Player()
player2 = Player()

player1.create_user("EF_Felix", "A_DUSENGIMANA")
for player in player1.login_user():
    print(player)