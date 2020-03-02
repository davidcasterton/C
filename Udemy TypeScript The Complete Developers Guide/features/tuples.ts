// object
const drink = {
    color: 'brown',
    carbonated: true,
    sugar: 40
};

// tuple - the type declaration  "[string, boolean, number]" makes this a tuple instead of array
let pepsi: [string, boolean, number] = ['brown', true, 40];

// tuple type declared
type Drink = [string, boolean, number];

let sprite: Drink = ['clear', true, 40];
let tea: Drink = ['brown', false, 0];

// tuple - easy to forget what should go in each index, not labeled with key
const carSpecs: [number, number] = [400, 3500];

// object - more readable because includes keys
const carStats = {
    horesePower: 400,
    weight: 3500,
};