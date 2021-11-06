.PHONY: install-deps
install-deps-linux:
	brew update
	brew upgrade
	brew tap ethereum/ethereum
	brew install solidity
	npm install ganache@alpha --global
	pip install -r requirements.txt
	brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0

.PHONY: build
build:
	brownie compile

.PHONY: test
test: build
	brownie test
