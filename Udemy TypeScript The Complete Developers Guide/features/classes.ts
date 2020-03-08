class Vehicle {
    public drive(): void {
        console.log('chugga chugga');
    }

    protected honk(): void {
        console.log('honk!');
    }
}

class Car extends Vehicle {
    public drive(): void {
        console.log('vroom');
    }

    private reverse(): void {
        console.log('beep, beep, beep');
    }

    public startReversing(): void {
        this.honk();
        this.reverse();
    }
}

const car = new Car();
car.startReversing();