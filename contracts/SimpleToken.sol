// contracts/PirataToken.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC721/ERC721.sol";
import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/access/Ownable.sol";


contract SimpleToken is ERC721Enumerable, Ownable {
    using Strings for uint256;

    uint256 public constant TOTAL_SUPPLY = 10;
    
    string private _tokenBaseURI = "https://my-json-server.typicode.com/freddyaboulton/pirata-token/tokens/";

    
    constructor() ERC721("SimpleToken", "STKN") { }
    
    
    function mint(uint256 tokenQuantity) external {
        require(totalSupply() < TOTAL_SUPPLY, "OUT_OF_STOCK");
        require(totalSupply() + tokenQuantity <= TOTAL_SUPPLY, "NOT_ENOUGH_IN_STOCK");
        
        for(uint256 i = 0; i < tokenQuantity; i++) {
            _safeMint(msg.sender, totalSupply() + 1);
        }        
    }
    
    function tokenURI(uint256 tokenId) public view override(ERC721) returns (string memory) {
        require(_exists(tokenId), "Cannot query non-existent token");
        
        return _tokenBaseURI;
    }
}
