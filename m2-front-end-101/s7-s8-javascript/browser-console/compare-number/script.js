const getUserInput = (message) => {
    let userInput;
    do {
        userInput = prompt(message);
        if (userInput === null) { //When the cancel button is clicked, prompt() returns null.
            alert("Operación cancelada");
            return null;
        }
    } while (isNaN(parseInt(userInput)) || userInput.trim() === ""); //"" represents an empty string, which is a valid string value but contains no characters.
    return parseInt(userInput);
};

const compareNumbers = () => {
    alert("Vamos a comparar qué número es mayor");

    const a = getUserInput("Introduce el primer número");
    if (a === null) return;
    const b = getUserInput("Introduce el segundo número");
    if (b === null) return;

    if (a === b) {
        alert(`${a} y ${b} son iguales`);
    } else if (a > b) {
        alert(`${a} es mayor que ${b}`);
    } else {
        alert(`${b} es mayor que ${a}`);
    }
};

compareNumbers();
