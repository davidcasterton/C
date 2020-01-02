#include <iostream>
#include <fstream>

#pragma pack(push, 1)  // turn on aligning data on byte boundaries
struct Person {
    char name[50];
    int age;
    double weight;
};
#pragma pack(pop)  // turn off aligning data on byte boundaries

int main() {
    std::cout << sizeof(Person) << std::endl;

    return 0;
}