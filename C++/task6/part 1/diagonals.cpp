#include <iostream>
#include <algorithm>
#include <vector>

void pretty_print_array(std::vector<std::vector<int>>& array) {
    /* Print 2D array to the console in a nice way */
    for (int i = 0; i < array.size(); i++) {
        std::cout << "[";
        for (int j = 0; j < array[i].size(); j++) {
            if (j == 0) {
                std::cout << array[i][j];
            }
            else {
                std::cout << " " << array[i][j];
            }
        }
        std::cout << "]" << std::endl;
    }
}

void pretty_print_vector(std::vector<int>& vector) {
    if (vector.size() != 0) {
        std::cout << "[";
    }
    for (int i = 0; i < vector.size(); i++) {
        if (i == vector.size() - 1) {
            std::cout << vector[i] << "]" << std::endl;
        }
        else {
            std::cout << vector[i] << ", ";
        }
    }
}


std::vector<std::vector<int>> create_array(int n) {
    /* Method to create a 2d array of random integers */
    srand(time(NULL));
    std::vector<std::vector<int>> array;
    for (int i = 0; i < n; i++) {
        std::vector<int> v;
        for (int j = 0; j < n; j++) {
            v.emplace_back(rand() % 9 + 1);
        }
        array.emplace_back(v);
        v = {};
    }
    return array;
}

std::vector<int> get_diagonal(std::vector<std::vector<int>>& array, int offset=0) {
    int size = array.size();
    if (offset > size || offset < -size) {
        std::cout << "Offset out of range" << std::endl;
        std::exit(0);
    }
    else {
        std::vector<int> diagonal;
        for (int i = 0; i < size; i++) {
            try {
                if (offset > 0) {
                    diagonal.emplace_back(array.at(i + offset).at(i));
                }
                else {
                    diagonal.emplace_back(array.at(i).at(i + abs(offset)));
                }
            }
            catch (const std::out_of_range& oor) {}
        }
        return diagonal;
    }
}

std::vector<std::vector<int>> get_all_diagonals(std::vector<std::vector<int>>& array, int m) {
    std::vector<int> diagonal;
    std::vector<std::vector<int>> diagonals;
    int size = array.size();

    for (int i = -(size - 1); i < size; i++) {
        diagonal = get_diagonal(array, i);
        if (diagonal.size() >= m) {
            diagonals.emplace_back(diagonal);
        }
    }

    return diagonals;
}

int get_min(std::vector<int>& array) {
    int min = array.at(0);
    for (int i : array) {
        if (i < min) {
            min = i;
        }
    }
    return min;
}

std::vector<int> vector_slice(std::vector<int>& array, int start, int end) {
    std::vector<int> newVector;
    for (int i = start; i < end; i++) {
        newVector.emplace_back(array[i]);
    }
    return newVector;
}

int smallest_sum_in_array(std::vector<int> array, int m) {
    int sum = 0;
    std::sort(array.begin(), array.end());
    array = vector_slice(array, 0, m);
    for (int i : array) {
        sum += i;
    }
    return sum;
}
