// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../VRFConsumer.sol";


contract VRFConsumerTest is VRFConsumer {

    constructor(bytes32 _keyhash, address _vrfCoordinator, address _linkToken, uint256 _fee) 
        VRFConsumer(_keyhash, _vrfCoordinator, _linkToken, _fee) {}

    function setRandomResult(uint256 _result) public {
        randomResult = _result;
    }

}