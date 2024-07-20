/*
1. Solicitar qué operación se desea realizar
2. Solicitar la cantidad de artículos comprados
3. Solicitar el precio de cada artículo
4. Calcular el total sin IVA
5. Calcular el total con IVA

- Calcular compra sin IVA
6.1 Mostrar el total sin impuestos

- Calcular compra con IVA
6.2 Mostrar el total con IVA incluido

- Calcular compra con descuento e IVA
6.3.1 Solicitar el porcentaje de descuento a aplicar
6.3.2 Mostrar el total con descuento y el total con IVA incluido */

const getUserPriceOrQuantityOrDiscountInput = (message) => {
	let userInput;
	do {
		userInput = prompt(message);
		if (userInput === null) {
			alert("Operación cancelada");
			return null;
		}
	} while (
		userInput.trim() == "" ||
		isNaN(parseInt(userInput)) ||
		parseInt(userInput) < 1
	);
	return parseInt(userInput);
};

const getUserOperationInput = (message) => {
	let userInput;
	do {
		userInput = prompt(message);
		if (userInput === null) {
			alert("Operación cancelada");
			return null;
		}
	} while (
		userInput.trim() == "" ||
		isNaN(parseInt(userInput)) ||
		parseInt(userInput) < 1 ||
		parseInt(userInput) > 3
	);
	return parseInt(userInput);
};

const calcIva = (total) => {
	return total * 0.19;
};

const productCalc = () => {
	// ANCHOR 1. Get operation
	const operationNumber = getUserOperationInput(
        "Introduce el número de la operación que deseas realizar: \n 1. Calcular compra sin IVA \n 2. Calcular compra con IVA \n 3. Calcular compra con IVA menos descuento"
	);
	if (operationNumber === null) return;

	// ANCHOR 2. Get product quantity and price
	const productQuantity = getUserPriceOrQuantityOrDiscountInput(
		"Introduce la cantidad de artículos comprados"
	);
	if (productQuantity === null) return;

	// ANCHOR 3. Get single product price
	const productPrice = getUserPriceOrQuantityOrDiscountInput(
		"Introduce el precio individual de tus artículos"
	);
	if (productPrice === null) return;

	// ANCHOR 4. Calculate total without IVA
	const total = productQuantity * productPrice;

    // ANCHOR 5. Calculate total with IVA
    const totalWithIva = total + calcIva(total);

	switch (operationNumber) {
		case 1:
            alert(`El total sin IVA es de ${total}`);
			break;
            
		case 2:
            alert(`El total con IVA es de ${totalWithIva}`);
			break;

		case 3:
            const discount = getUserPriceOrQuantityOrDiscountInput("Introduce el porcentaje de descuento a aplicar");
            let totalWithIvaMinusDiscount = totalWithIva - (totalWithIva * (discount / 100));
            alert(`El total con descuento e IVA es de ${totalWithIvaMinusDiscount}`);
			break;

		default:
            alert("Operación no válida");
			break;
	}

};

productCalc();
