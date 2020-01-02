#include <iostream>
#include <map>

int main() {

    std::multimap<int, std::string> lookup;
    lookup.insert(std::make_pair(30, "Dave"));
    lookup.insert(std::make_pair(10, "Mike"));
    lookup.insert(std::make_pair(30, "Jen"));
    lookup.insert(std::make_pair(20, "Jan"));

    for (std::multimap<int, std::string>::iterator it=lookup.begin(); it != lookup.end(); it++) {
        std::cout << it->first << " : " << it->second << std::endl;
    }
    std::cout << " -----" << std::endl;

    //std::pair<std::multimap<int, std::string>::iterator, std::multimap<int, std::string>::iterator> its = lookup.equal_range(30);
    auto its = lookup.equal_range(30);
    for (std::multimap<int, std::string>::iterator it=its.first; it != its.second; it++) {
        std::cout << it->first << " : " << it->second << std::endl;
    }

    return 0;
}
