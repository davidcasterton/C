#include <iostream>
#include <set>

class Test {
    int id;
    std::string name;

public:
    Test(): id(0), name("") {}
    Test(int id, std::string name): id(id), name(name) {}

    void print() const {
        std::cout << id << " : " << name << std::endl;
    }

    bool operator<(const Test &other) const {
        if (name == other.name) {
            return id < other.id;
        } else {
            return name < other.name;
        }
    }
};

int main() {

    std::set<int> numbers;

    // insert in set - only retains unique
    numbers.insert(10);
    numbers.insert(5);
    numbers.insert(5);
    numbers.insert(1);

    // iterate set
    for (auto it=numbers.begin(); it != numbers.end(); it++) {
        std::cout << *it << std::endl;
    }
    std::cout << " -----" << std::endl;

    // search for number
    int seach_num = 5;
    if (numbers.count(seach_num)) {
        std::cout << "Found " << seach_num << std::endl;
    }
    std::cout << " -----" << std::endl;

    // set of objects
    std::set<Test> tests;
    tests.insert(Test(1, "one"));
    tests.insert(Test(2, "second"));
    tests.insert(Test(1, "one"));

    for (auto it=tests.begin(); it != tests.end(); it++) {
        it->print();
    }

    return 0;
}
