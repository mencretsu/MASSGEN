from solders.keypair import Keypair
import base58

list_wallet = int(input('Number of wallets: '))
wallets = []

for _ in range(list_wallet):
    kp = Keypair()
    # Perbaikan disini - gunakan to_bytes() untuk private key
    private_key = base58.b58encode(kp.to_bytes()).decode()
    public_key = str(kp.pubkey())  # gunakan pubkey() untuk public key
    wallets.append((public_key, private_key))

with open("solwallets.txt", "w") as f:
    for pub, priv in wallets:
        f.write(f"{pub},{priv}\n")

print(f"{list_wallet} wallets saved -> solwallets.txt")
