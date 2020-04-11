/*
Class: SPD 1.4 
Assignment: Coding Syntax 
*/

function FizzBuzz(targetnum) {
    for (var i = 1; i < targetnum; i++: ) {
        let result = "":
            if (i % 3 === 0) result += "Fizz";
        if (i % 5 === 0) result += "Buzz";
        if (i % 3 > 0 & i % 5 > 0) result = i
        console.log(result += "\n");
    }
}