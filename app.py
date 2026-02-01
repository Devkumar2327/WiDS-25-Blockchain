from fastapi import FastAPI
from pydantic import BaseModel

from ml.model import predict_wallet
from security.hashing import generate_hash
from blockchain.web3_client import store_on_chain

app = FastAPI(title="Ethereum Fraud Detection API")

class WalletFeatures(BaseModel):
    wallet: str
    tx_count: int
    avg_value: float
    total_value: float
    unique_receivers: int
    active_days: float
@app.get("/")
def root():
    return {"status": "API running. Go to /docs"}

@app.post("/predict-and-store")
def predict_and_store(data: WalletFeatures):

    features = {
        "tx_count": data.tx_count,
        "avg_value": data.avg_value,
        "total_value": data.total_value,
        "unique_receivers": data.unique_receivers,
        "active_days": data.active_days
    }

    # 1. ML
    prediction, probability = predict_wallet(features)

    # 2. Hashing
    record, hash_hex = generate_hash(
        data.wallet, prediction, probability
    )

    # 3. Blockchain storage
    receipt = store_on_chain(hash_hex, prediction)

    return {
        "step": "Blockchain storage completed",
        "record": record,
        "hash": hash_hex,
        "blockchain_tx": receipt.transactionHash.hex()
    }



