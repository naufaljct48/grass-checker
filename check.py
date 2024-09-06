import requests

# Read all wallet addresses from wallets.txt per line
with open('wallets.txt', 'r') as file:
    wallet_addresses = [line.strip() for line in file.readlines()]

# Loop through each wallet address
for wallet_address in wallet_addresses:
    # API URL with the wallet address
    url = f'https://api.getgrass.io/airdropAllocations?input={{"walletAddress":"{wallet_address}"}}'
    
    # Request to the API for each wallet
    response = requests.get(url)
    data = response.json()

    # Extract result
    eligibility_data = data.get('result', {}).get('data', {})

    # Check for Sybil detection
    sybil_detected = any('sybil' in key.lower() for key in eligibility_data)

    # Check eligibility
    if sybil_detected:
        print(f'\033[93mAddress: {wallet_address} Detected as Sybil!\033[0m')
    elif eligibility_data:
        total_grass = sum(value for key, value in eligibility_data.items() if not 'sybil' in key.lower())
        print(f'\033[92mAddress: {wallet_address} Are Eligible! Total: {total_grass:.2f} $GRASS\033[0m')
    else:
        print(f'\033[91mAddress: {wallet_address} Not Eligible!\033[0m')
