// SPDX-License-Identifier: MIT
pragma solidity 0.8.30;

contract PersonalStorage {
    struct Note {
        string message;
        uint256 timestamp;
    }
    mapping(address => Note[]) private userNotes;
    uint256 public totalNotesCounter;
    function addNote(string memory _message) public {
        Note memory newNote = Note({
            message: _message,
            timestamp: block.timestamp
        });
        userNotes[msg.sender].push(newNote);
        totalNotesCounter++;
    }
    function getNotes() public view returns (Note[] memory) {
        return userNotes[msg.sender];
    }
}