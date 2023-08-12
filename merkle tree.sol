// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract MerkleTree {
    uint[] public leafNodes; // The leaf nodes of the Merkle tree
    uint public root; // The root node of the Merkle tree

    function addLeafNode(uint value) public {
        leafNodes.push(value);
        computeRoot(); // Recompute the root whenever a leaf node is added
    }

    function computeRoot() internal {
        root = 0; // Reset the root to zero

        for (uint i = 0; i < leafNodes.length; i++) {
            root += leafNodes[i]; // Sum up all leaf nodes
        }
    }

    function getRoot() public view returns (uint) {
        return root;
    }
}
