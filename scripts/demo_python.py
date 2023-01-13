import json
from web3 import Web3, HTTPProvider

def main():
    w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
    f = open('/Users/aayusharma/Downloads/code/smart_bank/usercode/bank/build/contracts/Bank.json')
    data = json.load(f)
    abi = data['abi']
    address = '0xA3348b0e5CeEBE47b308114bB2975b9123398e35'
    contract = w3.eth.contract(address=address,abi=abi)
    print(contract)

    isConnected = w3.isConnected()
    block_number = w3.eth.blockNumber
    print("Is connected:",isConnected,"/nBlock Number:",block_number)

    contract.functions.deposit_funds().transact({'from':w3.eth.accounts[2],'value':50})
    tx = contract.functions.transfer_funds(25,w3.eth.accounts[1]).transact({'from':w3.eth.accounts[2]})
    
    blocks = contract.functions.get_blocks().call({'from':w3.eth.accounts[2]})

    for num in blocks:
        block = w3.eth.get_block(num)
        tx = w3.eth.getTransaction(block.transactions[0])
        hist = contract.decode_function_input(tx.input)
        
        if str(hist[0])=='<Function deposit_funds()>':
            print("Funds Deposited:", tx.value)
        elif str(hist[0])=='<Function withdraw_funds(uint256)>':
            print("Funds Withdrawn:", hist[1]['_funds'])
        else:
            print("Funds transferred to account number", hist[1]['rec'],":",hist[1]['_funds'])
            