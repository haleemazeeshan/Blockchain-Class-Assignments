// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract ControlFlow {
// // while
//  function whileTest() public pure returns(uint256){
//  uint sum = 0;
//  uint i = 0;
//  while(i < 15){
//  sum += i;
//  i++; }
//  return(sum);
//  }
// }
/// For LOOP

    //  uint[] data;

    // function loop() public {
    //     for (uint8 i = 0; i < 20; i++) {
    //         if (i % 2 != 0) {
    //             data.push(i);
    //         }
    //     }
    // }

    // function getForloop() public view returns (uint[] memory) {
    //     return data;
    // }


//Do while loop
    uint[] data;

    function loop() public {
        uint8 i = 0;
        do {
            if (i % 2 != 0) {
                data.push(i);
            }
            i++;
        } while (i < 20);
    }

    function getDoWhile() public view returns (uint[] memory) {
        return data;
    }
}


