// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract Mapper{

    mapping(string => uint) public NameToBalance;
    
    function set(string memory _name, uint value) public {
        NameToBalance[_name] = value;
    }

    function get(string memory _name) public view returns (uint) {
        return NameToBalance[_name];
    }
}

