def rps_game_winner(*args):
    #RPS
    win_str = {
        'RP': ['player2', 'P'],
        'RS': ['player1', 'R'],
        'RR': ['player1', 'R'],
        'PS': ['player2', 'S'],
        'PR': ['player1', 'P'],
        'PP': ['player1', 'P'],
        'SS': ['player1', 'S'],
        'SP': ['player1', 'S'],
        'SR': ['player2', 'R'],       
    }
    if len(args[0])>2:
        raise Exception("WrongNumberOfPlayerError")
    if args[0][0][1].upper() not in 'RPS' or args[0][1][1].upper() not in 'RPS':
        raise Exception("NoSuchStrategyError")
    combination = str(args[0][0][1]) + str(args[0][1][1])

    return f'{win_str[combination][0]} {win_str[combination][1]}'

# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]), # => WrongNumberOfPlayersError
# rps_game_winner([['player1', 'P'], ['player2', 'A']]), #=> NoSuchStrategyError
# print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) #=> 'player2 S'
# # rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P')