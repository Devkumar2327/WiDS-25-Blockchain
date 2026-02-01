# WiDS-25-Blockchain
fraud_detection_project/
│
├── app.py                     # FastAPI entry point
│
├── ml/
│   └── model.py               # ML loading & prediction
│
├── security/
│   └── hashing.py             # SHA-256 hashing
│
├── blockchain/
│   ├── web3_client.py         # Web3 + Solidity calls
│   └── contract_abi.json      # ABI from Remix
│
├── xgb_fraud_model.pkl        # Trained ML model
├── .env                       # RPC + private key
└── requirements.txt

**Dataset link:** https://www.kaggle.com/datasets/chaitya0623/ethereum-transactions-for-fraud-detection?utm_source=chatgpt.com&select=first_order_df.csv
second_order_df.csv is used.


**Week 1:**
WidsA1: Assignment 1: performed on a house price dataset downloaded from Kaggle.
I performed data analysis tasks, i.e., data cleaning, handling missing values, detecting outliers, encoding, scaling, and performing PCA with and without scikit-learn.
Later, to check the efficiency, I predicted the score using RandomForestRegressor model ( because of the data's high dimensionality and complexity).
**Week 2:**
Studied MLE, MAP, SVM, Bayesian classification, and decision tree.
**Week 3:**
Assignment 2: Digital Notebook (Designed a smart contract for a personal storage system). learnt solidity basics, ledger basics, bitcoin architecture, data structures in solidity. 
**Week 4:**
A machine learning–based fraud detection system was implemented using an XGBoost classifier trained on behavioral Ethereum transaction features, with isError used as the fraud label. Alongside this, a Solidity smart contract was designed to store fraud detection results securely, and SHA-256 hashing was applied to generate cryptographic proofs of ML predictions before blockchain storage.
**Week 5:**
The machine learning pipeline was integrated with the blockchain through a FastAPI backend. The API handled ML inference, hash generation, and interaction with the Ethereum smart contract using Web3.py. The complete system was tested on a local Ethereum network (Ganache), achieving successful end-to-end execution and immutable storage of fraud detection results on the blockchain.
