import os
auction_continue = True
auction_dict = {}
while auction_continue:
    name = input('What is your name?\n')
    bid = input('What is your bid? \n$')
    auction_dict[name] = int(bid)
    a_cont = input('Is there another bidder? (y/n)').lower()
    if a_cont == 'n':
        auction_continue = False
    os.system('clear')

highest = 0
highest_name = ''
for name, bid in auction_dict.items():
    if bid >= highest:
        highest = bid
        highest_name = name

print(f'{highest_name} won the aution with a bid of ${auction_dict[highest_name]}')