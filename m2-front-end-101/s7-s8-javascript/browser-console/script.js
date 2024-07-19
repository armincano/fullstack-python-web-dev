const getUserInput = (message) => {
    let userInput;
    do {
        userInput = prompt(message);
        if (userInput === null) {
            alert("Operación cancelada");
            return null;
        }
    } while (isNaN(parseInt(userInput)) || userInput.trim() === ""); //lo parseado no es un número o está vacío
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
