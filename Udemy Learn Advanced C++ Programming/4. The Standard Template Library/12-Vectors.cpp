#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> strings(5);

    strings[0] = "cat";
    strings[1] = "bird";
    strings[3] = "dog";
    strings.push_back("one");
    strings.push_back("two");
    strings.push_back("three");

    std::cout << strings.size() << std::endl;

    // for loop
    for(int i=0; i < strings.size(); i++) {
        std::cout << strings[i] << std::endl;
    }

    // iterator
    std::cout << "iterator: " << std::endl;
    for(std::vector<std::string>::iterator it = strings.begin(); it != strings.end(); it++) {
        std::cout << *it << std::endl;
    }

    // auto iterator
    std::cout << "iterator 2: " << std::endl;
    for(auto it = strings.begin(); it != strings.end(); it++) {
        std::cout << *it << std::endl;
    }

    return 0;
}