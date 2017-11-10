#include <string>
#include "node.hpp"

class linked_list {
    public:
        linked_list() {}

        linked_list(node* firstNode) {
            head = firstNode;
            tail = firstNode;
        }

        node* head = nullptr;
        node* tail = nullptr;

        void push(node* newNode);
        void append(node* newNode);
        int size();
        void swap(node& a, node& b);
        void sort();
        bool isIn(std::string& word);

        friend std::ostream& operator<<(std::ostream& os, linked_list& list);
};
