import json, os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
account = w3.eth.account.from_key(os.getenv("PRIVATE_KEY"))

with open("blockchain/contract_abi.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(
    address=Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS")),
    abi=abi
)

def store_on_chain(hash_hex, prediction):
    nonce = w3.eth.get_transaction_count(account.address)

    tx = contract.functions.storeRecord(
        Web3.to_bytes(hexstr=hash_hex),
        True if prediction == 1 else False
    ).build_transaction({
        "from": account.address,
        "nonce": nonce,
        "gas": 300000,
        "gasPrice": w3.to_wei("20", "gwei")
    })

    signed_tx = w3.eth.account.sign_transaction(tx, os.getenv("PRIVATE_KEY"))
def store_on_chain(hash_hex, is_fraud):
    try:
        nonce = w3.eth.get_transaction_count(account.address)

        tx = contract.functions.storeRecord(
            Web3.to_bytes(hexstr=hash_hex),
            bool(is_fraud)
        ).build_transaction({
            "from": account.address,
            "nonce": nonce,
            "gas": 300000,
            "gasPrice": w3.to_wei("20", "gwei")
        })

        signed_tx = w3.eth.account.sign_transaction(tx, account.key)

        tx_hash = w3.eth.send_raw_transaction(
            signed_tx.raw_transaction
        )

        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

    except Exception as e:
        print("🔥 BLOCKCHAIN ERROR:", e)
        raise

