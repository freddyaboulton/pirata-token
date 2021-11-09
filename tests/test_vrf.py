import pytest

@pytest.fixture
def vrf_contract(VRFConsumerTest, accounts, history):
    yield VRFConsumerTest.deploy(accounts[0].address, accounts[0].address, accounts[0].address,
                                 0, {'from': accounts[0]})


def test_can_request_random_number(vrf_contract, accounts):
    vrf_contract.setRandomResult(100)
    assert vrf_contract.randomResult() == 100
    assert not vrf_contract.isRandomResultGreaterThan(123)