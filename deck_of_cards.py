# deck_of_cards.py
# کار با دسته ورق

import random

# تعریف رنگ‌ها و رتبه‌ها
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']

# 1. انتخاب یک کارت تصادفی
rank = random.choice(RANKS)
suit = random.choice(SUITS)
print("کارت تصادفی:", rank + ' of ' + suit)

# 2. ایجاد کل دسته ورق
deck = []
for rank in RANKS:
    for suit in SUITS:
        card = rank + ' of ' + suit
        deck += [card]

print("تعداد کارت‌ها:", len(deck))

# 3. بر زدن دسته (الگوریتم)
n = len(deck)
for i in range(n):
    r = random.randrange(0, i + 1)
    # جابه‌جایی کارت‌ها
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

print("۵ کارت اول بعد از بر زدن:", deck[:5])