from brownie import PirataToken, accounts

N_TOKENS = 3

def deploy():
    return PirataToken.deploy("PirataToken", "PRT", "http://127.0.0.1:8000/tokens/", {'from': accounts[0]})

def mint(token, n_tokens):
    for i in range(n_tokens):
        transaction = token.mint(accounts[i].address)
        transaction.wait(1)


def main():
    token = deploy()
    mint(token, n_tokens=N_TOKENS)

