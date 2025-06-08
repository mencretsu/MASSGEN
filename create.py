from eth_account import Account

list_wallet = int(input('Number of wallets: '))
wallets = []

for _ in range(list_wallet):
    acct = Account.create()
    wallets.append((acct.address, acct.key.hex()))

with open("wallets.txt", "w") as f:
    for addr, key in wallets:
        f.write(f"{addr},{key}\n")

print(f"{list_wallet} Saved -> wallets.txt")
