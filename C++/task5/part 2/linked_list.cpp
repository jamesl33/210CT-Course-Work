#include <iostream>
#include <string>
#include "linked_list.hpp"

void linked_list::push(node* newNode) {
    if (head == nullptr && tail == nullptr) {
        head = newNode;
        tail = newNode;
    } else {
        newNode -> next = head;
        newNode -> previous = nullptr;
        head -> previous = newNode;
        head = newNode;
    }
}

void linked_list::append(node* newNode) {
    if (head == nullptr && tail == nullptr) {
        head = newNode;
        tail = newNode;
    } else {
        newNode -> next = nullptr;
        newNode -> previous = tail;
        tail -> next = newNode;
        tail = newNode;
    }
}

bool linked_list::isIn(std::string& word) {
    node* currentNode = head;
    while (currentNode != nullptr) {
        if (currentNode -> data == word) {
            return true;
        }
        currentNode = currentNode -> next;
    }
    return false;
}

int linked_list::size() {
    int count = 0;
    node* currentNode = head;
    while (currentNode != nullptr) {
        count++;
        currentNode = currentNode -> next;
    }
    return count;
}

void linked_list::swap(node& a, node& b) {
    auto tmpData = b.data;
    b.data = a.data;
    a.data = tmpData;
}

void linked_list::sort() {
    bool sorted = false;
    node* currentNode = head;

    while (!sorted) {
        sorted = true;
        while (currentNode != nullptr) {
            if (currentNode -> next != nullptr && currentNode -> data > currentNode -> next -> data) {
                sorted = false;
                swap(*currentNode, *currentNode -> next);
            }
            currentNode = currentNode -> next;
        }
        currentNode = head;
    }
}

std::ostream& operator<<(std::ostream& os, linked_list& list) {
    node* currentNode = list.head;
    while (currentNode != nullptr) {
        if (currentNode == list.head) {
            os << "[" << currentNode -> data << ", ";
        } else if (currentNode -> next == nullptr) {
            os << currentNode -> data << "]";
        } else {
            os << currentNode -> data << ", ";
        }
        currentNode = currentNode -> next;
    }
    return os;
}
