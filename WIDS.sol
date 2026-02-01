// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FraudDetectionStorage {

    struct Record {
        bytes32 dataHash;
        bool isFraud;
        uint256 timestamp;
    }

    mapping(bytes32 => Record) private records;

    event RecordStored(
        bytes32 indexed dataHash,
        bool isFraud,
        uint256 timestamp
    );

    function storeRecord(bytes32 _dataHash, bool _isFraud) public {
        require(
            records[_dataHash].timestamp == 0,
            "Record already exists"
        );

        records[_dataHash] = Record({
            dataHash: _dataHash,
            isFraud: _isFraud,
            timestamp: block.timestamp
        });

        emit RecordStored(_dataHash, _isFraud, block.timestamp);
    }

    function getRecord(bytes32 _dataHash)
        public
        view
        returns (bool isFraud, uint256 timestamp)
    {
        require(
            records[_dataHash].timestamp != 0,
            "Record not found"
        );

        Record memory r = records[_dataHash];
        return (r.isFraud, r.timestamp);
    }
}
