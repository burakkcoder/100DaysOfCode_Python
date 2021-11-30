import art

print(art.logo)

bidders = {}

while True:
    name = input("What is your name?\n")
    bid = input("What's your bid?\n")
    bidders[name] = bid

    other = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if other == "yes":
        print("\n" * 10)
        continue
    else:
        bidders = sorted(bidders.items(), key=lambda x: x[1], reverse=True)
        print(f"The winner is {bidders[0][0]} with a bid of ${bidders[0][1]}")
        break