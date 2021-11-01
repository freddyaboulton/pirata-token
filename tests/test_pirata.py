import pytest

INITIAL_VALUE = 4

@pytest.fixture
def pirata_contract(pirata, accounts):
    # deploy the contract with the initial value as a constructor argument
    yield pirata.deploy({'from': accounts[0]})


def test_supports_er615_interface(pirata_contract):
    # Check if the constructor of the contract is set up properly
    assert pirata_contract.supportsInterface(0x0000000000000000000000000000000000000000000000000000000001ffc9a7)


def test_supports_er721_interface(pirata_contract):
    assert pirata_contract.supportsInterface(0x0000000000000000000000000000000000000000000000000000000001ffc9a7)


def test_balance_of_is_zero(pirata_contract, accounts):
    assert pirata_contract.balanceOf(accounts[1]) == 0


def test_balance_of_zero_account_raises(pirata_contract):
    with pytest.raises(ValueError, match="is not a valid ETH address"):
        pirata_contract.balanceOf(0x0000000000000000000000000000000000000000)