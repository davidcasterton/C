// interface - a variable of sorts that defines types
interface Vehicle {
    name: string;
    year: Date;
    broken: boolean;
    summary(): string;  // a function that returns a string
};

interface Reportable {
    summary(): string;
};

// object
const oldCivic = {
    name: 'civic',
    year: new Date(),
    broken: true,
    summary(): string {
        return `$name: ${this.name}`;
    }
};

const drink_ = {
    color: 'brown',
    carbonated: true,
    sugar: 40,
    summary(): string {
        return `my drink has ${this.sugar} grams of sugar`;
    }
};

// WITHOUT INTERFACE
// argument named vehicle of type {name: string; year: number; broken: boolean}
// return type void
// const printVehicle = (vehicle: {name: string; year: number; broken: boolean}): void => {
//     console.log(`name: ${vehicle.name}`);
//     console.log(`year: ${vehicle.year}`);
//     console.log(`broken: ${vehicle.broken}`);
// };
// printVehicle(oldCivic);

// WITH INTERFACE
const printSummary = (item: Reportable): void => {
    console.log(item.summary());
};
// TS checks to make sure that oldCivic has all properties defined in Vehicle 
printSummary(oldCivic);

printSummary(drink_);