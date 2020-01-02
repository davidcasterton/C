#include <iostream>
#include <fstream>

#pragma pack(push, 1)  // turn on aligning data on byte boundaries
struct Person {
    char name[50];
    int age;
    double height;
};
#pragma pack(pop)  // turn off aligning data on byte boundaries

int main() {
    Person someone = {"Frodo", 220, 0.8};
    Person someoneElse = {};

    std::string fileName = "11-example.bin";

    std::ofstream outFile;
    outFile.open(fileName, std::ios::binary);
    if(outFile.is_open()) {
        // outFile.write((char *)&someone, sizeof(someone));
        outFile.write(reinterpret_cast<char *>(&someone), sizeof(Person));
        outFile.close();
    }
    else {
        std::cout << "Could not create file: " << fileName << std::endl;
    }

    std::ifstream inFile;
    inFile.open(fileName, std::ios::binary);
    if(inFile.is_open()) {
        inFile.read(reinterpret_cast<char *>(&someoneElse), sizeof(Person));
        inFile.close();
    }
    else {
        std::cout << "Could not open file: " << fileName << std::endl;
    }

    std::cout << someoneElse.name << ", " << someoneElse.age << ", " << someoneElse.height << std::endl;

    return 0;
}
