const carMakers: string[] = ['ford', 'toyota', 'chevy'];
const dates = [new Date(), new Date()];
// 2D array
let carsByMake: string[][] = [];
carsByMake = [
    ['f150'],
    ['corolla'],
    ['camaro']
];

// 1) help inference when extracting values
const car_ = carMakers[0];
const myCar = carMakers.pop();

// 2) prevent incompatible values
carMakers.push(100);

// 3) can get help from built-in functions
carMakers.map((car: string): string => {
    return car.toUpperCase();
});

// 4) flexible types
const importantDates: (Date | string)[] = [new Date()];
importantDates.push('2030-10-10');
importantDates.push(new Date());
