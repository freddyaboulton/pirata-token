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
    assert not simple_token_contract.IS_PRESALE()
    assert not simple_token_contract.IS_SALE()


def test_presale_mint(simple_token_contract, accounts):
    simple_token_contract.setPresale(True, {'from': accounts[0]})

    simple_token_contract.addToPresale([accounts[0]], {'from': accounts[0]})
    simple_token_contract.mintPresale(1, {'from': accounts[0], 'value': "1 wei"})
    assert simple_token_contract.ownerOf(1) == accounts[0]
    assert simple_token_contract.balanceOf(accounts[0]) == 1
    assert simple_token_contract.totalSupply() == 1
    assert simple_token_contract.tokenURI(1) == "https://my-json-server.typicode.com/freddyaboulton/pirata-token/tokens/1"
    assert simple_token_contract.balance() == "1 wei"


def test_cannot_pint_presale_if_not_on_list(simple_token_contract, accounts):
    simple_token_contract.setPresale(True, {'from': accounts[0]})
    with pytest.raises(VirtualMachineError, match="NOT ON PRESALE"):
        simple_token_contract.mintPresale(1, {'from': accounts[1], 'value': "1 wei"})


def test_multiple_people_can_mint_presale(simple_token_contract, accounts):
    simple_token_contract.setPresale(True, {'from': accounts[0]})
    simple_token_contract.addToPresale(accounts[:4], {'from': accounts[0]})

    simple_token_contract.mintPresale(1, {'from': accounts[1], 'value': "1 wei"})
    simple_token_contract.mintPresale(2, {'from': accounts[2], 'value': "2 wei"})
    simple_token_contract.mintPresale(1, {'from': accounts[3], 'value': "1 wei"})

    assert simple_token_contract.balanceOf(accounts[1]) == 1
    assert simple_token_contract.balanceOf(accounts[2]) == 2
    assert simple_token_contract.balanceOf(accounts[3]) == 1

    assert simple_token_contract.ownerOf(1) == accounts[1]
    
    for i in range(2, 4):
        assert simple_token_contract.ownerOf(i) == accounts[2]

    assert simple_token_contract.ownerOf(4) == accounts[3]


def test_cannot_buy_if_out_of_stock(simple_token_contract, accounts):
    simple_token_contract.setPresale(True, {'from': accounts[0]})
    simple_token_contract.addToPresale([accounts[1], accounts[3], accounts[5]], {'from': accounts[0]})
    simple_token_contract.mintPresale(4, {'from': accounts[1], 'value': "4 wei"})
    
    with pytest.raises(VirtualMachineError, match="NOT_ENOUGH_IN_STOCK"):
        simple_token_contract.mintPresale(2, {'from': accounts[3], 'value': "2 wei"})

    simple_token_contract.mintPresale(1, {'from': accounts[5], 'value': '1 wei'})

    with pytest.raises(VirtualMachineError, match="OUT_OF_STOCK"):
        simple_token_contract.mintPresale(2, {'from': accounts[7], 'value': "2 wei"})


def test_can_mint_during_sale(simple_token_contract, accounts):
    simple_token_contract.setSale(True, {'from': accounts[0]})
    simple_token_contract.mint(1, {'from': accounts[4], 'value': "1 wei"})
    simple_token_contract.mint(2, {'from': accounts[5], 'value': "2 wei"})
    assert simple_token_contract.balanceOf(accounts[4]) == 1
    assert simple_token_contract.balanceOf(accounts[5]) == 2
