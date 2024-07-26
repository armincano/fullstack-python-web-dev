/*
{trayectoria del control de flujo} {descripción función}

1 bienvenida app - alert
1 Ingresar RUN -prompt numbers
1 Ingresar contraseña -prompt strings
1 validar RUN y contraseña

1.1 Si el RUN y la contraseña son incorrectos, alert mensaje de error
1.1 Volver a ingresar RUN

1.2 Si el RUN y la contraseña son correctos,mostrar mensaje de bienvenida account
1.2 mostrar menú -prompt numbers

1.2.1 checkBalance -alert saldo
1.2.1 volver a menu

1.2.2 makeWithdrawal
1.2.2 mostrar el monto actual + ingresar retiro
1.2.2 validar que no gire un valor mayor que el saldo actual.
1.2.2.1 si no es valido, mostrar error
1.2.2.2 si es valido, -actualizar saldo - mostrar saldo actualizado

1.2.3 makeDeposit
1.2.3 mostrar el monto actual + ingresar deposito
1.2.3 actualizar saldo - mostrar saldo actualizado


1.2.4 exit */

//SECTION - Texts
const welcomeAppMsg = "Bienvenido a Banca en Línea";
const runAuthMsg = "Ingresa tu RUN\nPuedes usar el RUN 123, 456 o 789 siendo la contraseña igual al RUN utilizado";
const passwordAuthMsg = "Intrega tu contraseña";
const wrongCredentialsMsg =
	"Tus credenciales son incorrectas, inténtalo nuevamente";
const invalidOptionMsg = "Opción inválida, inténtalo nuevamente";
const closeSessionMsg = "Hasta luego";
const menuMsg =
	"Selecciona una opción: \n1. Consultar saldo \n2. Realizar retiro \n3. Realizar depósito \n4. Salir";

const balanceMsg = (balance) => `Tu saldo es de ${balance}`;
const whithdrawalAmountMsg = "Ingresa el monto que desea girar:";
const whithdrawalSuccessMsg = (balance) => `Giro realizado con éxito. Tu saldo actual es de: ${balance}`;
const whithdrawalInsuficientBalanceMsg = "Tu saldo es insuficiente para realizar la operación.";

const depositAmountMsg = "Ingresa el monto que desea depositar:";
const depositSuccessMsg = (balance) => `Depósito realizado con éxito. Tu saldo actual es de: ${balance}`;


//!SECTION - Texts

//SECTION - usersDb
const usersDb = [
	{
		run: 123,
		password: "123",
		name: "Juan",
		balance: 100000,
	},
	{
		run: 456,
		password: "456",
		name: "Diego",
		balance: 50000,
	},
	{
		run: 789,
		password: "789",
		name: "Pedro",
		balance: 500,
	},
];
//!SECTION - usersDb

//SECTION - Functions
//ANCHOR - stringInput
const stringInput = (message) => {
	let userInput;
	do {
		userInput = prompt(message);
		if (userInput === null) return null;
	} while (userInput.trim() === "");
	return userInput.toString();
};

//ANCHOR - numberInput
const numberInput = (message) => {
	do {
		userInput = prompt(message);
		if (userInput === null) return null;
	} while (
		isNaN(parseInt(userInput)) ||
		userInput.trim() === "" ||
		parseInt(userInput) < 1
	);
	return parseInt(userInput);
};

//ANCHOR - checkCredentials
const checkCredentials = (userRun, userPassword) => {
	let userIndex = [false, 0];
	for (const user of usersDb) {
		if (user.run == userRun && user.password == userPassword) {
			userIndex = [true, usersDb.indexOf(user)];
			return userIndex;
		}
	}
	return userIndex;
};

//ANCHOR - checkBalance
const checkBalance = (userIndex) => {
	return usersDb[userIndex].balance;
};

//ANCHOR - updateBalanceWithdrawal
const updateBalanceWithdrawal = (userIndex, whithdrawalAmount) => {
	usersDb[userIndex].balance -= whithdrawalAmount;
	return usersDb[userIndex].balance;
}

//ANCHOR - updateBalanceDeposit
const updateBalanceDeposit = (userIndex, depositAmount) => {
	usersDb[userIndex].balance += depositAmount;
	return usersDb[userIndex].balance;
}

//ANCHOR - makeWhithdrawal
const makeWithdrawal = (userIndex) => {
	let balance = checkBalance(userIndex);
	let whithdrawalAmount = numberInput(`${balanceMsg(balance)}\n${whithdrawalAmountMsg}`);
	if (whithdrawalAmount === null) return;

	if (whithdrawalAmount > balance) {
		alert(whithdrawalInsuficientBalanceMsg);
		return;
	}

	if (whithdrawalAmount <= balance) {
		balance = updateBalanceWithdrawal(userIndex, whithdrawalAmount);
		alert(whithdrawalSuccessMsg(balance));
	}
}

//ANCHOR - makeDeposit
const makeDeposit = (userIndex) => {
	let balance = checkBalance(userIndex);
	let depositAmount = numberInput(`${balanceMsg(balance)}\n${depositAmountMsg}`);
	if (depositAmount === null) return;

	balance = updateBalanceDeposit(userIndex, depositAmount);
	alert(depositSuccessMsg(balance));
}

//!SECTION - Functions

//SECTION - Account
const accountApp = (userCredentials) => {
	userInput = numberInput(menuMsg);
	if (userInput === null) return;

	switch (userInput) {
		case 1:
			let balanceMessage = balanceMsg(checkBalance(userCredentials[1]));
			alert(balanceMessage);
			break;
		case 2:
			makeWithdrawal(userCredentials[1]);
			break;
		case 3:
			makeDeposit(userCredentials[1]);
			break;
		case 4:
			alert(closeSessionMsg);
			return true;
		default:
			alert(invalidOptionMsg);
			break;
	}
};
//!SECTION - Account

//SECTION - Login
const bankingApp = () => {
	let userCredentials = [false, 0];
	let closeSession = false;

	alert(welcomeAppMsg)

	const userRunInput = numberInput(runAuthMsg);
	if (userRunInput === null) return;

	const userPasswordInput = stringInput(passwordAuthMsg);
	if (userPasswordInput === null) return;

	userCredentials = checkCredentials(userRunInput, userPasswordInput);
	if (!userCredentials[0]) {
		alert(wrongCredentialsMsg);
		bankingApp();
	}else{
		do {
			closeSession = accountApp(userCredentials);
		} while (!closeSession);
	}
	
};

bankingApp();
//!SECTION - Login
