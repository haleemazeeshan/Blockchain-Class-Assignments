//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ExamContract {
    enum Exam { None, Checking, Pass, Fail, Scholarship }

    Exam public e1;

    function Pass() public {
        if (e1 == Exam.Checking) {
            e1 = Exam.Pass;
           
        }
    }

    function Fail() public {
        if (e1 == Exam.Checking) {
            e1 = Exam.Fail;
        }
    }

    function Scholarship() public {
        if (e1 == Exam.Pass) {
            e1 = Exam.Scholarship;
        }
    }

    function idelete() public {
            delete e1;
    }
}
