.PHONY: install-deps
install-deps-linux:
	sudo add-apt-repository ppa:ethereum/ethereum
	sudo apt-get update
	sudo apt-get install solc
	npm install ganache@alpha --global
	pip install -r requirements.txt
	brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0

.PHONY: build
build:
	brownie compile

.PHONY: test
test: build
	brownie test
