# gambler_ruin.py
# شبیه‌سازی ورشکستگی قمارباز

import sys
import random

stake = int(sys.argv[1])   # سرمایه اولیه
goal = int(sys.argv[2])    # هدف
trials = int(sys.argv[3])  # تعداد آزمایش

bets = 0
wins = 0

for t in range(trials):
    cash = stake
    while 0 < cash < goal:
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print(str(100 * wins // trials) + '% wins')
print('Avg # bets: ' + str(bets // trials))