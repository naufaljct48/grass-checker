import requests

# Membaca semua wallet address dari file wallets.txt per line
with open('wallets.txt', 'r') as file:
    wallet_addresses = [line.strip() for line in file.readlines()]

# Loop melalui setiap wallet address
for wallet_address in wallet_addresses:
    # API URL with the wallet address
    url = f'https://api.getgrass.io/airdropAllocations?input={{"walletAddress":"{wallet_address}"}}'
    
    # Request ke API untuk setiap wallet
    response = requests.get(url)
    data = response.json()

    # Extract result
    eligibility_data = data.get('result', {}).get('data', {})

    # Cek eligibility
    if eligibility_data:
        total_grass = sum(eligibility_data.values())
        print(f'\033[92mAddress: {wallet_address} Are Eligible! Total: {total_grass:.2f} $GRASS\033[0m')
    else:
        print(f'\033[91mAddress: {wallet_address} Not Eligible!\033[0m')
