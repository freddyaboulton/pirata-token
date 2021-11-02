# Pirata Token
<p align="center">
<img width=50% src="https://twitter.github.io/twemoji/v/13.1.0/svg/1f3f4-200d-2620-fe0f.svg" alt="Pirate Flag" />
</p>

An example NFT deployed to a local blockchain. Implemented and tested on OSX 10.15.17.

# Installation

1. **Writing Contracts**: Install [solidity](https://docs.soliditylang.org/en/v0.8.9/installing-solidity.html#macos-packages) with homebrew.
2. **Local Ethereum Blockchain**: Install [ganache-cli](https://github.com/trufflesuite/ganache#getting-started).
3. **Python Requirements**: `pip install -r requirements.txt`. This installs [brownie](https://eth-brownie.readthedocs.io/en/stable/index.html),
a development framework for smart contracts, fast-api, a python library for writting apis, as well as vyper, a smart contract language based on python.

# Project Overview

* `contracts/`: Source code for our contracts. One is written in Solidity, the other is written in vyper.
* `scripts/`: Scripts for deploying our NFT smart contract and minting three NFTs on a local blockchain.
* `server/`: Small backend used to display the NFT metadata.
* `tests/`: Unit tests.

# How to run

1. Start the local blockchain: `ganache-cli`
2. Deploy our contract and mint some NFTs: `brownie run deploy_and_mint_local.py main`
3. Start the server: `uvicorn server.main:app`. Go to the `tokens/{token_id}` end point to see the token metadata.
