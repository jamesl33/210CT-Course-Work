#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <algorithm>
#include <map>
#include "linked_list.hpp"

void remove_punctuation(std::string& word) {
    for (int i = 0, len = word.size(); i < len; i++)
    {
        if (ispunct(word[i]))
        {
            word.erase(i--, 1);
            len = word.size();
        }
    }
}

int main() {
    linked_list list = linked_list();
    std::map<int, linked_list> linkedListMap;

    std::fstream file;
    file.open("paragraph.txt");

    if (!file) {
        std::cerr << "Unable to open file datafile.txt";
        std::exit(1);
    }

    std::string word;
    while (file >> word) {
        remove_punctuation(word);
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);
        node* newNode = new node(word);

        if (linkedListMap.count(word.size()) > 0) {
            if (!(linkedListMap[word.size()].isIn(word))) {
                linkedListMap[word.size()].append(newNode);
            }
        }
        else {
            linkedListMap[word.size()] = linked_list();
            linkedListMap[word.size()].append(newNode);
        }
    }

    for (std::map<int, linked_list>::iterator it=linkedListMap.begin(); it!=linkedListMap.end(); it++) {
        it -> second.sort();
        std::cout << it -> first << ": " << it -> second << std::endl;
    }
}
