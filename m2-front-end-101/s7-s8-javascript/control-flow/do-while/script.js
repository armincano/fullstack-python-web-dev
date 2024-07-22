const menuMsg = "1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit";

let userInput;

do {
    userInput = parseInt(prompt(menuMsg));
} while (userInput !== 5);