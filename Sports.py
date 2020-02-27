# All the information related to the sports news through some inbuilt functions

import sports
all_matches=sports.all_matches()
cricket=all_matches['cricket']
#print(cricket)
matches=sports.get_sport(sports.TENNIS)
print(matches)
