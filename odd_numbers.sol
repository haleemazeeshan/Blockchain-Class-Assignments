// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Loop {
     uint[] data;

    function loop() public {
        for (uint8 i = 1; i <= 20; i = i + 2) {
            data.push(i);
        }
    }

    function getOddNumbers() public view returns (uint[] memory) {
        return data;
    }
}
