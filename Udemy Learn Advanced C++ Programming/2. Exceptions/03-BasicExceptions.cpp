#include <iostream>

void mightGoWrong() {
    bool error1 = false;
    bool error2 = true;

    if (error1) {
        throw 8;
    }
    if (error2) {
        throw std::string("string error");
    }
}

int main() {
    
    try {
        mightGoWrong();
    }
    catch(int e) {
        std::cout << "Error code: " << e << std::endl;
    }
    catch(char const * e) {
        std::cout << "Error message: " << e << std::endl;
    }
    catch(std::string &e) {
        std::cout << "String error message: " << e << std::endl;
    }
    std::cout << "Still running" << std::endl;

    return 0;
}