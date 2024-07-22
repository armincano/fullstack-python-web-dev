/*
1. welcome: Elegir opción - Validar número

2.1 receiptAndPayment/Boleta y pagos: Elegir opción + validar número
2.1.1 Opción 1 - Mostrar mensaje
2.1.2 Opción 2 - Mostrar mensaje

2.2 signalAndCallIssues/Señal y llamadas: Elegir opción + validar número
2.2.1 Opción 1 - Escribir solicitud
2.2.1.1 Mostrar solicitud
2.2.2 Opción 2 - Escribir solicitud
2.2.1.1 Mostrar solicitud

2.3 offers/Oferta comercial: Elegir opción + Validar Sí o No
2.3.1 Sí - Mostrar mensaje
2.3.2 No - Mostrar mensaje

2.4 miscDoubts/Otras consultas: Escribir solicitud
2.4.1 Mostrar solicitud

2.5 Opción inválida: Mostrar mensaje */

//SECTION - Constants
const doHaveNewDoubt = "¿Tiene otra duda?";

const invalidOptionMsg = "Opción inválida.";

const endApp = "Gracias por preferir nuestros servicios.";

const welcomeMsg =
	"¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas";

const receiptAndPayment1 =
	"Seleccione una opción\n1.- Ver Boleta\n2.- Pagar cuenta";
const receiptAndPayment1i1 = "Haga clic aquí para descargar su boleta.";
const receiptAndPayment1i2 =
	"Usted está siendo transferido. Espere por favor...";

const signalAndCallIssues2 =
	"Seleccione una opción\n1.- Problemas con la señal\n2.- Problemas con las llamadas";
const signalAndCallIssues2a = "Problemas con la señal";
const signalAndCallIssues2b = "Problemas con las llamadas";
const signalAndCallIssues2i1 =
	"A continuación escriba detalles para su solicitud:";
const signalAndCallIssues2i1i1Msg = (issue, details) =>
	`Estimado usuario, su solicitud: <${details}> relacionada con <${issue}>, ha sido ingresada con éxito.\nPronto será contactado por uno de nuestros ejecutivos.`;

const offers3 =
	"¡Mentel tiene una oferta comercial acorde a tus necesidades!\nPara conocer más información y ser asesorado personalmente por un ejecutivo escribe 'Sí' y un ejecutivo te llamará. De lo contrario ingrese 'NO'";
const offers3i1 = "Un ejecutivo contactará con usted";
const offers3i2 = "Gracias por preferir nuestros servicios";

const miscDoubts4 = "A continuación escriba detalles para su solicitud:";
const miscDoubts4i1 = (details) =>
	`Estimado usuario, su consulta: <${details}> ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.`;

//!SECTION - Constants

//SECTION - Generic Functions

const writeNumberOption = (message) => {
	let userInput;
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

const writeStringOption = (message) => {
	let userInput;
	do {
		userInput = prompt(message);
		if (userInput === null) return null;
	} while (userInput.trim() === "");
	return userInput;
};
//!SECTION - Generic Functions

//SECTION - L1 sections
const doRepeatApp = () => {
	const doRepeatApp = confirm(doHaveNewDoubt);
	if (!doRepeatApp) {
		alert(endApp);
		return;
	} else {
		virtualBoxApp();
	}
};
//!SECTION - L1 sections

//SECTION - L2 sections
//SECTION - 1 - receiptAndPayment/Boleta y pagos
const receiptAndPayment = () => {
	const userInput = writeNumberOption(receiptAndPayment1);
	if (userInput === null) return;

	switch (userInput) {
		case 1:
			alert(receiptAndPayment1i1);
			break;
		case 2:
			alert(receiptAndPayment1i2);
			break;

		default:
			alert(invalidOptionMsg);
			break;
	}
};
//!SECTION - 1 - receiptAndPayment/Boleta y pagos

//SECTION - 2 - signalAndCallIssues/Señal y llamadas
const signalAndCallIssues = () => {
	let details;

	const userInput = writeNumberOption(signalAndCallIssues2);
	if (userInput === null) return;

	switch (userInput) {
		case 1:
			details = writeStringOption(signalAndCallIssues2i1);
			if (details === null) return;
			alert(signalAndCallIssues2i1i1Msg(signalAndCallIssues2a, details));
			break;
		case 2:
			details = writeStringOption(signalAndCallIssues2i1);
			if (details === null) return;
			alert(signalAndCallIssues2i1i1Msg(signalAndCallIssues2b, details));
			break;
		default:
			alert(invalidOptionMsg);
			break;
	}
};
//!SECTION - 2 - signalAndCallIssues/Señal y llamadas

//SECTION - 3 - offers/Oferta comercial
const offers = () => {
	let userInput = writeStringOption(offers3);
	if (userInput === null) return;

	let normalizedUserInput = userInput.toLowerCase().trim().replace(/í/g, "i");
	switch (normalizedUserInput) {
		case "si":
			alert(offers3i1);
			break;
		case "no":
			alert(offers3i2);
			break;
		default:
			alert(invalidOptionMsg);
			break;
	}
};
//!SECTION - 3 - offers/Oferta comercial

//SECTION - 4 - miscDoubts/Otras consultas
const miscDoubts = () => {
	let userInput = writeStringOption(miscDoubts4);
	if (userInput === null) return;

	alert(miscDoubts4i1(userInput));
};
//!SECTION - 4 - miscDoubts/Otras consultas
//!SECTION - L2 sections

//SECTION - L1 section: Main App
const virtualBoxApp = () => {
	const userInput = writeNumberOption(welcomeMsg);

	switch (userInput) {
		case 1:
			receiptAndPayment();
			break;

		case 2:
			signalAndCallIssues();
			break;

		case 3:
			offers();
			break;

		case 4:
			miscDoubts();
			break;

		case null:
			break;

		default:
			alert(invalidOptionMsg);
			break;
	}

	doRepeatApp();
};

virtualBoxApp();
//!SECTION - L1 section: Main App
