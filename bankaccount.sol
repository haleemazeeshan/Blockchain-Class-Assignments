// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    struct BankAccount {
        uint256 accountID;
        uint256 balance;
        address owner;
    }

    BankAccount public accounts;
    function Method1() public {
        BankAccount storage newAccount = accounts;
            newAccount.accountID= 1234567;
            newAccount.balance= 100000;
            newAccount.owner= 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
        
    }

    function Method2() public {
        
        accounts.accountID= 1234567;
        accounts.balance= 100000;
        accounts.owner= 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    }

    function Method3() public {
        accounts=BankAccount(1234567, 100000, 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4);
    }

    function Method4() public {
            accounts= BankAccount({
            accountID: 1234567,
            balance: 100000,
            owner: 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
        });
        
    }

    function get() public view returns (uint256, uint256, address) {
        return (accounts.accountID, accounts.balance, accounts.owner);
    }

}
