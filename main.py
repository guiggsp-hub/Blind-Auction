print("Welcome to Blind Auction Project")
print( r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


name_and_bid = {}

name=input("What is your name? ")
price=float(input("What is your bid? R$"))

name_and_bid[name] = price

should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
print('\n'*50)
while True:
    name = input("What is your name? ")
    price = float(input("What is your bid? R$"))
    name_and_bid[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print('\n'*50)
    if should_continue == "no":
        break

print('The winner is:',end=' ')
print(max(name_and_bid, key= name_and_bid.get),end=' ')
