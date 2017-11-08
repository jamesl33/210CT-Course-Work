#include <string>

class node {
public:
    node(std::string d) {
        data = d;
    }

    std::string data;
    node* previous = nullptr;
    node* next = nullptr;
};
