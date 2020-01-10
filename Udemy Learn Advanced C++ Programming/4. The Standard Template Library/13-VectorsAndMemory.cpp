#include <iostream>
#include <vector>

int main() {
    std::vector<double> numbers(10);
    int capacity = numbers.capacity();

    std::cout << "Size: " << numbers.size() << std::endl;
    std::cout << "Capacity: " << numbers.capacity() << std::endl;

    for(int i=0; i<10000; i++) {
        
        numbers.push_back(i);
        
        if(numbers.capacity() != capacity) {
            capacity = numbers.capacity();
            std::cout << "Capacity: " << capacity << std::endl;
        }
    }

    return 0;
}
