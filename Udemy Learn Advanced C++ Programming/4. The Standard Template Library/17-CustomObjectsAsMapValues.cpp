#include <iostream>
#include <map>

class Person {
private:
    std::string name;
    int age;

public:
    Person(): name(""), age(0) {}
    Person(const Person &other) {
        std::cout << "copy constructor" << std::endl;
        name = other.name;
        age = other.age;
    }
    Person(std::string name, int age) : name(name), age(age) {}
    void print() const {
        std::cout << name << " : " << age << std::endl;
    }
};

int main() {
    std::map<int, Person> people;
    people[0] = Person("Mike", 40);
    people[1] = Person("Vicky", 30);
    people[2] = Person("Raj", 20);

    people.insert(std::make_pair(55, Person("Bob", 45)));
    people.insert(std::make_pair(55, Person("Sue", 55)));

    for (std::map<int, Person>::iterator it = people.begin(); it != people.end(); it++) {
        std::cout << it->first << " : " << std::flush;
        it->second.print();
    }

    return 0;
}
