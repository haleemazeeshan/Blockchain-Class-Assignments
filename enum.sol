//SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;
contract PizzaDeli {
    enum PizzaOrder { None, Preparing, Received }

    PizzaOrder public P1;
    PizzaOrder public P2;
    PizzaOrder public P3;

    // constructor() {
    //     // Method 1
    //     P1 = PizzaOrder.None;
    //     P2 = PizzaOrder.Preparing;
    //     // Method 2
    //     P3 = PizzaOrder.Received;
    // }
// Setter function for P1 variable
    function setP1Status(PizzaOrder status) external {
        P1 = status;
    }

    // Getter function to return values of P1, P2, and P3
    function getPizzaStatuses() external view returns (PizzaOrder, PizzaOrder, PizzaOrder) {
        return (P1, P2, P3);
    }
}

            