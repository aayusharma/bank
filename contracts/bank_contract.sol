//SPDX-License-Identifier: MIT 
pragma solidity ^0.8.17;

contract Bank{
    mapping(address => uint) private account_balance;
    mapping(address => uint[]) private blocks;
    function deposit_funds() public payable{
        account_balance[msg.sender] += msg.value;
        blocks[msg.sender].push(block.number);
    }
    function withdraw_funds(uint _funds) public {    
        require(account_balance[msg.sender]>=_funds,"Insufficient Balance");
        account_balance[msg.sender]-= _funds;
        (bool success,) = msg.sender.call{value: _funds}("Amount Withdrawn");
        require(success,"Insufficient Balance");
        blocks[msg.sender].push(block.number);
    }
    function transfer_funds(uint _funds, address payable rec) public {
        require(account_balance[msg.sender]>=_funds,"Insufficient Balance");
        account_balance[msg.sender]-= _funds;
        account_balance[rec] += _funds;
        blocks[msg.sender].push(block.number);
        blocks[rec].push(block.number);
    }
    function get_balance() public view returns(uint){
        return account_balance[msg.sender];
    }
    function get_blocks() public view returns(uint[] memory){
        return blocks[msg.sender];
    }
}