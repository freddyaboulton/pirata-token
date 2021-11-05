import pytest

from brownie.exceptions import VirtualMachineError

INITIAL_VALUE = 4

@pytest.fixture
def simple_token_contract(SimpleToken, accounts):
    # deploy the contract with the initial value as a constructor argument
    yield SimpleToken.deploy({'from': accounts[0]})


def test_init(simple_token_contract, accounts):
    assert accounts[0].address == simple_token_contract.owner()
    assert simple_token_contract.TOTAL_SUPPLY() == 10


def test_owner_can_mint(simple_token_contract, accounts):
    simple_token_contract.mint(1, {'from': accounts[0]})
    assert simple_token_contract.ownerOf(1) == accounts[0]
    assert simple_token_contract.balanceOf(accounts[0]) == 1
    assert simple_token_contract.totalSupply() == 1

def test_multiple_people_can_mint(simple_token_contract, accounts):
    simple_token_contract.mint(1, {'from': accounts[1]})
    simple_token_contract.mint(3, {'from': accounts[2]})
    simple_token_contract.mint(4, {'from': accounts[3]})

    assert simple_token_contract.balanceOf(accounts[1]) == 1
    assert simple_token_contract.balanceOf(accounts[2]) == 3
    assert simple_token_contract.balanceOf(accounts[3]) == 4

    assert simple_token_contract.ownerOf(1) == accounts[1]
    
    for i in range(2, 5):
        assert simple_token_contract.ownerOf(i) == accounts[2]

    for i in range(5, 9):
        assert simple_token_contract.ownerOf(i) == accounts[3]

def test_cannot_buy_if_out_of_stock(simple_token_contract, accounts):
    tx = simple_token_contract.mint(9, {'from': accounts[1]})
    tx.wait(0.1)
    
    with pytest.raises(VirtualMachineError, match="NOT_ENOUGH_IN_STOCK"):
        tx = simple_token_contract.mint(2, {'from': accounts[3]})
        tx.wait(.2)

    tx = simple_token_contract.mint(1, {'from': accounts[5]})
    tx.wait(0.2)

    with pytest.raises(VirtualMachineError, match="OUT_OF_STOCK"):
        tx = simple_token_contract.mint(2, {'from': accounts[7]})
        tx.wait(0.2)
