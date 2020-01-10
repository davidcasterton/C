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
        std::cout << name << " : " << age << std::flush;
    }
    bool operator<(const Person &other) const {
        if (name == other.name) {
            return age < other.age;
        } else {
            return name < other.name;
        }
    }
};

int main() {
    std::map<Person, int> people;
    people[Person("Mike", 40)] = 1;
    people[Person("Dave", 20)] = 2;
    people[Person("Jeff", 30)] = 3;

    people.insert(std::make_pair(Person("Bob", 45), 4));
    people.insert(std::make_pair(Person("Sue", 55), 5));
    people[Person("Mike", 35)] = 6;

    for (std::map<Person, int>::iterator it = people.begin(); it != people.end(); it++) {
        it->first.print();
        std::cout << " : " << it->second << std::endl;
    }

    return 0;
}
