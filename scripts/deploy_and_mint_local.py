from brownie import PirataToken, accounts

N_TOKENS = 3

def deploy():
    return PirataToken.deploy({'from': accounts[0]})

def mint(token, n_tokens):
    for i in range(n_tokens):
        transaction = token.mint(1, {'from': accounts[i]})
        transaction.wait(1)

def main():
    token = deploy()
    mint(token, n_tokens=N_TOKENS)

