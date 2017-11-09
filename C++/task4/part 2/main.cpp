#include <iostream>
#include <vector>
#include <limits>
#include "quick_sort.cpp"

int main() {
    srand(time(NULL));
    std::vector<int> unsortedArray;

    for (int i = 0; i < 10; i++) {
        unsortedArray.emplace_back(rand() % 1000);
    }

    quick_sort(unsortedArray, 0, unsortedArray.size() - 1);

    for (int i : unsortedArray) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "Which element would you like to find? (0 indexed) ";
    int input = 0;
    while (true) {
        if (!(std::cin >> input)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input.  Try again: ";
        } else if (input > unsortedArray.size() - 1) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Input out of range for array.  Try again: ";
        } else {
            std::cout << "The element in index " << input << " is " << unsortedArray[input] << std::endl;
            break;
        }
    }
}
