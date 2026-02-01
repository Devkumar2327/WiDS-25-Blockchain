import hashlib
import json
from datetime import datetime

def generate_hash(wallet, prediction, probability):
    record = {
        "wallet": wallet,
        "prediction": "Fraud" if prediction == 1 else "Legit",
        "probability": round(probability, 4),
        "timestamp": datetime.utcnow().isoformat()
    }

    json_string = json.dumps(record, sort_keys=True)
    hash_hex = hashlib.sha256(json_string.encode()).hexdigest()

    return record, hash_hex
