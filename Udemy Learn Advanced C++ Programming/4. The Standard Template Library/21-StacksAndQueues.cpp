#include <iostream>
#include <stack>
#include <queue>

class Test {
public:
    Test(std::string name): name(name) {}
    ~Test() {
        std::cout << name << " destroyed" << std::endl;
    }
    void print() {
        std::cout << name << std::endl;
    }

private:
    std::string name;

};

int main() {

    // stacks are last in first out (LIFO)
    // push onto top of stack
    // pop off top of stack
    std::cout << "STACKS:" << std::endl;

    std::stack<Test> testStack;
    testStack.push(Test("Mike"));
    testStack.push(Test("Dave"));
    testStack.push(Test("Jeff"));
    testStack.push(Test("Kyle"));
    testStack.push(Test("Brian"));

    std::cout << " - top, then pop:" << std::endl;
    Test test1 = testStack.top();  // returns element
    test1.print();
    testStack.pop();  // does not return element, just removes it

    // NOTE: this is invalid, object is destroyed before use
    // Test &test2 = testStack.top();
    // testStack.pop();
    // test2.print();

    std::cout << " - top:" << std::endl;
    Test test3 = testStack.top();
    test3.print();

    int i = 0;
    while (testStack.size() > 0) {
        std::cout << i++ << " : " << std::flush;

        Test &test = testStack.top();
        test.print();
        testStack.pop();
    }

    // queues are first in first out (FIFO)
    std::cout << "QUEUES:" << std::endl;

    std::queue<Test> testQueue;
    testQueue.push(Test("Mike"));
    testQueue.push(Test("Dave"));
    testQueue.push(Test("Jeff"));
    testQueue.push(Test("Kyle"));
    testQueue.push(Test("Brian"));

    testQueue.back().print();
    std::cout << std::endl;

    i = 0;
    while (testQueue.size() > 0) {
        std::cout << i++ << " : " << std::flush;

        Test &test = testQueue.front();  // returns element
        test.print();
        testQueue.pop();  // removes element
    }

    return 0;
}
