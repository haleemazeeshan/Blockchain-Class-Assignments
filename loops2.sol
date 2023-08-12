// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract Loop{
 uint[] public arr;
 function NaturalNum(uint max) public returns(uint[] memory){
 uint i = 1;
 while(i <= max){
 arr.push(i);
 i++;
 }
 return arr; }
 }