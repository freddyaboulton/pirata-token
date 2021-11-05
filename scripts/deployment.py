from brownie import SimpleToken, accounts

def main():
    acct = accounts.load('personal')
    SimpleToken.deploy({'from': acct})