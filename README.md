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

Week 1:
WidsA1: Assignment 1: performed on a house price dataset downloaded from Kaggle.
I performed data analysis tasks, i.e., data cleaning, handling missing values, detecting outliers, encoding, scaling, and performing PCA with and without scikit-learn.
Later, to check the efficiency, I predicted the score using RandomForestRegressor model ( because of the data's high dimensionality and complexity).
Week 2: 
Studies MLE, MAP, SVM, Bayesian classification and decision tree.
Week 3:
Assignment 2: Digital Notebook (Designed a smart contract for a personal storage system). learnt solidity basics, ledger basics, bitcoin architecture, data structures in solidity. 
