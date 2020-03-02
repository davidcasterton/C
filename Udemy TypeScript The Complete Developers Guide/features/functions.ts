const add = (a: number, b: number): number => {
    return a + b;
};


const subtract = (a: number, b: number): number => {
    return a - b;
};

const divide = (a: number, b: number): number => {
    return a / b;
};

const multiply = (a: number, b: number): number => {
    return a * b;
};

// void
const logger = (message: string): void => {
    console.log(message);
}

// never
const throwError = (message: string): never => {
    throw new Error(message);
}

// destructuring with annotations
const todaysWeather = {
    date: new Date(),
    weather: 'sunny'
};
// WITHOUT DESTRUCTURE:     const logWeather = (forecast: {date: Date, weather: string}): void => {
const logWeather = ({date, weather}: {date: Date, weather: string}): void => {
    console.log(date);
    console.log(weather);
}
logWeather(todaysWeather);

// ES2015 destructuring syntax
// const logWeather2 = ({date, weather}) => {
//     console.log(date);
//     console.log(weather);
// }