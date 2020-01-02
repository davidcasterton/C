#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> ages;

    ages["Mike"] = 40;
    ages["Dave"] = 20;
    ages["Jeff"] = 30;

    // print element
    std::cout << ages["Mike"] << std::endl;
    std::cout << " -----" << std::endl;

    // insert pair to map
    std::pair<std::string, int> addToMap("Peter", 100);
    ages.insert(addToMap);

    // insert pair to map using make_pair
    ages.insert(std::make_pair("John", 200));

    // iterate map
    for(std::map<std::string, int>::iterator it=ages.begin(); it != ages.end(); it++) {
        std::cout << it->first << " : " << it->second << std::endl;
    }
    std::cout << " -----" << std::endl;

    // iterate map, using pair
    for(std::map<std::string, int>::iterator it=ages.begin(); it != ages.end(); it++) {
        std::pair<std::string, int> age = *it;
        std::cout << age.first << " : " << age.second << std::endl;
    }
    std::cout << " -----" << std::endl;

    // find
    if(ages.find("Dave") != ages.end()) {
        std::cout << "Found Dave!" << std::endl;
    }
    else {
        std::cout << "Could not find Dave" << std::endl;
    }

    return 0;
}
