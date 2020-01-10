// showing exceptions can be thrown from constructors
#include <iostream>

class CanGoWrong {
public:
    CanGoWrong() {
        char *pMemory = new char[99999999999999999999999];
        delete[] pMemory;
    }
};

int main() {
    try {
        CanGoWrong wrong;
    }
    catch(std::bad_alloc &e) {
        std::cout << "Caught exception: " << e.what() << std::endl;
    }
    std::cout << "Strill running" << std::endl;

    return 0;
}
