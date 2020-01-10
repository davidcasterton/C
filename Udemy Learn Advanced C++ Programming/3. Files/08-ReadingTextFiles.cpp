#include <iostream>
#include <fstream>

int main() {
    std::ifstream inFile;
    std::string fileName = "07-example.txt";

    inFile.open(fileName);

    if (inFile.is_open()) {
        std::string line;

        while (!inFile.eof()) {
            std::getline(inFile, line);
            std::cout << line << std::endl;
        }

        inFile.close();
    }
    else {
        std::cout << "Could not open file: " << fileName << std::endl;
    }

    return 0;
}