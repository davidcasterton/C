#include <iostream>
#include <list>

int main() {
    std::list<int> numbers;

    // push_back, push_front
    numbers.push_back(1);
    numbers.push_back(2);
    numbers.push_back(3);
    numbers.push_back(4);
    numbers.push_front(0);

    // insert
    std::list<int>::iterator it = numbers.begin();
    it++;
    numbers.insert(it, 100);
    std::cout << "Element: " << *it << std::endl;

    // erase
    it = numbers.begin();
    it++;
    numbers.erase(it);
    std::cout << "Element: " << *it << std::endl;

    // iterator
    for(std::list<int>::iterator it = numbers.begin(); it != numbers.end(); it++) {
        std::cout << *it << std::endl;
    }

    return 0;
}
