const BACKPACK = {
    name: 'Everyday Backpack',
    volume: 30,
    printHi: function() {
        console.log(`Hi! My name is ${this.name}`);
    }
}
BACKPACK.printHi(); // Hi

// Constructor Function
function Animal(type, sound) {
	this.type = type;
    this.sound = sound;
	this.makeSound = function() { console.log(this.sound); };
}

Animal.prototype.jump = function() {
    console.log(`The ${this.type} jumped!`);
};

const DOG_A = new Animal("Dog", "Bark");
const CAT_A = new Animal("Cat", "Meow");

DOG_A.jump(); // "The Dog jumped!"
CAT_A.jump(); // "The Cat jumped!"
// Change the method on the prototype
Animal.prototype.jump = function() {
    console.log(`The ${this.type} jumped higher!`);
};
DOG_A.jump(); // "The Dog jumped higher!"
CAT_A.jump(); // "The Cat jumped higher!"

DOG_A.makeSound(); // "Bark"
CAT_A.makeSound(); // "Meow"
// Changing the method defined in the constructor function and not through the prototype doesn't work
Animal.prototype.makeSound = function() {
    console.log(`The ${this.type} makes a sound`);
};
DOG_A.makeSound(); // "Bark"
CAT_A.makeSound(); // "Meow"
const SNAKE_A = new Animal("Snake", "Ssssss");
SNAKE_A.makeSound(); // "Ssssss"

// Factory Function with object literal syntax
const createAnimal = (type, sound) => {
	return {
		type: type,
		sound: sound,
		jump: function() {
			console.log(`The ${this.type} jumped!`);
		},
		makeSound: function() {
			console.log(this.sound);
		},
	};
};

const DOG_B = createAnimal("Dog", "Bark");
const CAT_B = createAnimal("Cat", "Meow");


