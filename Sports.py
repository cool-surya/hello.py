import sports
all_matches=sports.all_matches()
cricket=all_matches['cricket']
#print(cricket)
matches=sports.get_sport(sports.TENNIS)
print(matches)