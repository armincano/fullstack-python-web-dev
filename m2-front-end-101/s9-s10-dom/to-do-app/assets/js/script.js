//SECTION - tasksDb
const tasks = [
	{ task: "Pintar la fachada de la casa", isCompleted: false },
	{ task: "Comprar comida para el perro", isCompleted: false },
	{ task: "Pagar la tarjeta de crédito", isCompleted: false },
];
const emptyTasks = [{ task: "No hay tareas pendientes", isCompleted: true }];
//!SECTION - tasksDb

//SECTION - DOM retreive elements
const addTasksBtn = document.getElementById("addTasksBtn");

const newTaskInput = document.getElementById("newTaskInput");
const addSingleTaskBtn = document.getElementById("addSingleTaskBtn");

const tasksForm = document.getElementById("tasksForm");
const tasksTableBody = document.getElementById("tasksTableBody");
//!SECTION - DOM retreive elements

//SECTION - Functions

//ANCHOR - toggleHidden
const toggleHidden = (element) => element.classList.toggle("hidden");

//ANCHOR - toggleIsCompleted property value
const eraseTasksTableBodyAndRenderTasks = () => {
	tasksTableBody.innerHTML = "";
	renderTasks();
};

//ANCHOR - insertTaskToArray
const pushTaskToArray = (taskInput) => {
	tasks.push({ task: taskInput, isCompleted: false });
	newTaskInput.value = "";
	eraseTasksTableBodyAndRenderTasks();
};

const toggleIsCompleted = (idx) => {
	tasks[idx].isCompleted = !tasks[idx].isCompleted;
	eraseTasksTableBodyAndRenderTasks();
};

//ANCHOR - deleteTask
const deleteTask = (idx) => {
	tasks.splice(idx, 1);
	eraseTasksTableBodyAndRenderTasks();
};

//ANCHOR - createAndAppendTaskTableRow
const createAndAppendTaskTableRow = ({ task, isCompleted }, idx) => {
	const tableRow = document.createElement("tr");
	const tableData1 = document.createElement("td");
	const tableData2 = document.createElement("td");
	const tableData3 = document.createElement("td");
	const completeButton = document.createElement("button");
	const deleteButton = document.createElement("button");

	tableData1.textContent = task;
	if (isCompleted) {
		tableData1.classList.add("text-decoration-line-through");
	}
	completeButton.classList.add("btn", "btn-primary");
	completeButton.textContent = "👍";
	completeButton.addEventListener("click", () => toggleIsCompleted(idx));
	deleteButton.classList.add("btn", "btn-danger");
	deleteButton.textContent = "⏏️";
	deleteButton.addEventListener("click", () => deleteTask(idx));

	tableData2.appendChild(completeButton);
	tableData3.appendChild(deleteButton);
	tableRow.appendChild(tableData1);
	tableRow.appendChild(tableData2);
	tableRow.appendChild(tableData3);
	tasksTableBody.appendChild(tableRow);
};

//ANCHOR - renderTasks
const renderTasks = () => {
	if (tasks.length === 0) {
		const tableRow = document.createElement("tr");
		const tableData1 = document.createElement("td");
        tableData1.textContent = "No hay tareas pendientes";
        tableRow.appendChild(tableData1);
        tasksTableBody.appendChild(tableRow);
	} else {
		tasks.map((singleTask, idx) => {
			createAndAppendTaskTableRow(singleTask, idx);
		});
	}
};
//!SECTION - Functions

//SECTION - Event Listeners
addTasksBtn.addEventListener("click", () => toggleHidden(tasksForm));

addSingleTaskBtn.addEventListener("click", () =>
	pushTaskToArray(newTaskInput.value)
);
//!SECTION - Event Listeners

//SECTION - Initial Render
renderTasks();
//!SECTION - Initial Render
