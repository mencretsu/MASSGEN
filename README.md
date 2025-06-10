# MASSGEN
Mass wallet generator for BSC/ETH/Polygon and Solana networks.

## Files
- `create.py` - For BSC/ETH/Polygon wallets
- `createsol.py` - For Solana wallets

## Requirements
```bash
# For BSC/ETH/Polygon
pip install eth-account

# For Solana
pip install solders base58
```

## Output
Wallets will be saved as: `address,private_key` format
- BSC/ETH/Polygon -> `wallets.txt`
- Solana -> `solwallets.txt`
