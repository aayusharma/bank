import json
from brownie import Bank, accounts, chain
from web3 import Web3, HTTPProvider
def main():
    w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
    f = open('/Users/aayusharma/Downloads/code/smart_bank/usercode/bank/build/contracts/Bank.json')
    data = json.load(f);
    abi = data['abi'];
    address = '0xA3348b0e5CeEBE47b308114bB2975b9123398e35'
    bank_contract = Bank.at(address)
    contract = w3.eth.contract(address=address,abi=abi)

    # bank_contract.deposit_funds({'from':accounts[1],'value':150})
    # print("Balance of Account 1:",bank_contract.get_balance({'from':accounts[1]}))

    # bank_contract.transfer_funds(50, accounts[2], {'from':accounts[1]})

    # print("Balance of account 1:", bank_contract.get_balance({'from':accounts[1]}))
    # print("Balance of account 2:", bank_contract.get_balance({'from':accounts[2]}))
 
    # bank_contract.withdraw_funds(50, {'from':accounts[1]})
    # print("Balance of account 1:", bank_contract.get_balance({'from':accounts[1]}))
 
    # print("Blocks of account 2:", bank_contract.get_blocks({'from':accounts[2]}))
    blocks = bank_contract.get_blocks({'from':accounts[1]})
    for num in blocks:

        block = chain[num]

        tx = w3.eth.getTransaction(block.transactions[0])

        hist = contract.decode_function_input(tx.input)

        if str(hist[0]) == '<Function deposit_funds()>':
            print("Funds Deposited:", tx.value)
        elif str(hist[0]) == '<Function withdraw_funds(uint256)>':
            print("Funds Withdrawn:", hist[1]['_funds'])
        else:
            print("Funds transferred to account number", hist[1]['rec'], ":", hist[1]['_funds'])