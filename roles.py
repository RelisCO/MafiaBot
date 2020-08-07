mafia, don, civilian, sheriff = 'Mafia', 'Don', 'Civilian', 'Sheriff'
minimum, maximum = 4, 7
roles = {'4': [civilian]*3+[don], '5': [civilian]*4+[don],
         '6': [civilian]*3+[don]+[mafia]+[sheriff],
         '7': [civilian]*4+[don]+[mafia]+[sheriff]}
