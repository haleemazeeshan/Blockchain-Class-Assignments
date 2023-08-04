
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TicketBookingSystem {
    enum TicketType { Economy, Business, FirstClass }

    enum Days { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday }

    struct Ticket {
        string passenger;
        TicketType ticketType;
        Days day;
        bool isBooked;
    }

    Ticket[] public tickets;

    function bookTicket(string memory _passenger, Days _day,TicketType _ticketType) public {
        Ticket memory newTicket = Ticket({
            passenger: _passenger,
            ticketType: _ticketType,
            day: _day,
            isBooked: false
        });
        tickets.push(newTicket);
    }

    function getTicketType(uint256 _index) public view returns (TicketType) {
        return tickets[_index].ticketType;
    }

    function getTicketDay(uint256 _index) public view returns (Days) {
              return tickets[_index].day;
    }

    function toggleStatus(uint256 _index) public {
        if (tickets[_index].isBooked) {
            tickets[_index].isBooked = false; 
        } else {
            tickets[_index].isBooked = true; 
        }
      }
}
