// variables
const apples: number = 5;
let bananas: number = 8;
bananas = 10;
let speed: string = 'fast';
let notMuch: null = null;
let nothing: undefined = undefined;
let now: Date = new Date();

// array
let colors: string[] = ['red', 'green', 'blue'];
let numbers_: number[] = [1,2,3];
let truths: boolean[] = [true, true, false];

// classes
class Car {

}
let car: Car = new Car();

// object literal
let point: {x: number; y: number} = {
    x: 10,
    y: 20
};

// function
// "(i: number) => void" says input arg of i with type number, return type void
const logNumber: (i: number) => void = (i: number) => {
    console.log(i);
}

// when you *need* annotations
// 1) function that returns the 'any' type
const json = '{"x": 10, "y": 20}';
const coordinates : {x: number; y: number} = JSON.parse(json);
console.log(coordinates);

// 2) when we declare a variable on 1 line and initialize it later
let words = ['red', 'green', 'blue'];
let foundWord: boolean;
for (let i = 0; i < words.length; i++) {
    if (words[i] === 'green') {
        foundWord = true;
    }
}

// 3) variable whose type cannot be inferred correctly
let numbers = [-10, -1, 12];
let numberAboveZero: boolean | number = false;
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > 0) {
        numberAboveZero = numbers[i];
    }
}

