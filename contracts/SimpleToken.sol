// contracts/PirataToken.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC721/ERC721.sol";
import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/access/Ownable.sol";


contract SimpleToken is ERC721Enumerable, Ownable {
    using Strings for uint256;

    uint256 public constant TOTAL_SUPPLY = 10;
    uint public constant PRESALE_SUPPLY = 5;
    uint public constant SALE_SUPPLY = 5;
    uint public constant SALE_PRICE = 1 wei;
    mapping (address => bool) private presaleList;
    bool public IS_PRESALE = false;
    bool public IS_SALE = false;
    
    string private _tokenBaseURI = "https://my-json-server.typicode.com/freddyaboulton/pirata-token/tokens/";

    constructor() ERC721("SimpleToken", "STKN") { }
    
    function addToPresale(address[] calldata _addresses) external onlyOwner {
        for(uint i = 0; i < _addresses.length; i++){
            address account = _addresses[i];
            require(account != address(0), "Invalid Address!");
            require(!presaleList[account], "Already on presale list");
            presaleList[account] = true;
        }
    }

    function mintPresale(uint tokenQuantity) external payable {
        require(msg.value >= SALE_PRICE * tokenQuantity, "NOT_ENOUGH_MONEY");
        require(IS_PRESALE, "NOT PRESALE");
        require(tokenQuantity > 0, "Invalid Token Quantity");
        require(totalSupply() < PRESALE_SUPPLY, "OUT_OF_STOCK");
        require(totalSupply() + tokenQuantity <= PRESALE_SUPPLY, "NOT_ENOUGH_IN_STOCK");
        require(presaleList[msg.sender], "NOT ON PRESALE");
        for(uint i = 0; i < tokenQuantity; i++){
            _safeMint(msg.sender, totalSupply() + 1);
        }
    }
    
    function mint(uint256 tokenQuantity) external payable {
        require(IS_SALE, "NOT SALE");
        require(totalSupply() < TOTAL_SUPPLY, "OUT_OF_STOCK");
        require(totalSupply() + tokenQuantity <= TOTAL_SUPPLY, "NOT_ENOUGH_IN_STOCK");
        
        for(uint256 i = 0; i < tokenQuantity; i++) {
            _safeMint(msg.sender, totalSupply() + 1);
        }        
    }
    
    function tokenURI(uint256 tokenId) public view override(ERC721) returns (string memory) {
        require(_exists(tokenId), "Cannot query non-existent token");
        
        return string(abi.encodePacked(_tokenBaseURI, tokenId.toString()));
    }

    function setPresale(bool value) external onlyOwner {
        IS_PRESALE = value;
    }

    function setSale(bool value) external onlyOwner {
        IS_SALE = value;
    }
}
