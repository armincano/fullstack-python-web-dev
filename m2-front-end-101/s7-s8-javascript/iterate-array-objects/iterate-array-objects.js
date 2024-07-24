const students = [
	{ name: "Jonh", grade: 75 },
	{ name: "Jane", grade: 93 },
	{ name: "Samantha", grade: 90 },
	{ name: "Michael", grade: 94 },
];

console.log(students);

// 3. Ordenar el arreglo en orden descendente (mayor a menor) basados en su calificacion
students.sort((a,b) => b.grade - a.grade);
console.log(students);

// 2. Invertir la orden del arreglo
students.reverse();
console.log(students);

// 3. Encontrar el primer estudiante con calificación mayor a 90
const firstStudentAbove90 = students.find(student => student.grade > 90);
console.log('Primer estudiante con calificación mayor a 90:', firstStudentAbove90);