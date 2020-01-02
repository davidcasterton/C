#include <iostream>
#include <fstream>

int main() {
    std::ifstream input;
    std::string fileName = "stats.txt";

    input.open(fileName);

    if(!input.is_open()) {
        return 1;
    }

    std::string line;
    int population;
    while(input) {
        std::getline(input, line, ':');
        input >> population;
        input.get();

        std::cout << "'" << line << "'" << " -- " << "'" << population << "'" << std::endl;
    }

    input.close();

    return 0;
}