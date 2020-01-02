#include <iostream>
#include <fstream>

int main() {
    std::ofstream outFile;
    std::string outputFileName = "07-example.txt";

    outFile.open(outputFileName);

    if (outFile.is_open()) {
        outFile << "Line 1" << std::endl;
        outFile << "Line 2" << std::endl;
        outFile.close();
    }
    else {
        std::cout << "Could not create file: " << outputFileName << std::endl;
    }

    return 0;
}