// catch subclasses before parent classes, because parent classes can also catch
#include <iostream>
#include <exception>

void goesWrong() {
    bool error1detected = true;
    bool error2detected = false;

    if (error1detected) {
        throw std::bad_alloc();
    }
    if (error2detected) {
        throw std::exception();
    }
}

int main() {

    try {
        goesWrong();
    }
    catch(std::bad_alloc &e) {
        std::cout << "bad_alloc: " << e.what() << std::endl;
    }
    catch(std::exception &e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }

    return 0;
}