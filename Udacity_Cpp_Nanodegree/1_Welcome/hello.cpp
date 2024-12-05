#include <iostream>
#include <string>
#include <vector>

int main() {
  //   std::cout << "Hello, world!" << std::endl;
  std::vector<std::string> brothers{"John", "Paul", "George", "Ringo"};
  for (std::string brother : brothers) {
    std::cout << "Hello, " << brother << "!" << std::endl;
  }

  return 0;
}
