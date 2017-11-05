#include <vector>
#include <tuple>
#include <algorithm>
#include <iostream>

std::vector<std::vector<int>> create_array(int n, int m) {
    /* Method to create a 2d array of random integers */
    srand(time(NULL));
    std::vector<std::vector<int>> array;
    for (int i = 0; i < n; i++) {
        std::vector<int> v;
        for (int j = 0; j < m; j++) {
            v.emplace_back(rand() % 10);
        }
        array.emplace_back(v);
        v = {};
    }
    return array;
}

std::vector<std::tuple<int, int>> check_neighbours(std::vector<std::vector<int>>& array, int x, int y) {
    /* Method to check if the neighbours of coords (x, y) are of the same Color/Number as "(x, y)".
    returns vector of tuples representing (x, y) coords of neighbours which have the same color/number as "(x, y)" */
    std::vector<std::tuple<int, int>> neighbours;

    if (!x - 1 < 0) {
        if (array[x - 1][y] == array[x][y]) {
            neighbours.emplace_back(x - 1, y);
        }
    }

    if (!((x + 1) > (array.size() - 1))) {
        if (array[x + 1][y] == array[x][y]) {
            neighbours.emplace_back(x + 1, y);
        }
    }

    if (!y - 1 < 0) {
        if (array[x][y - 1] == array[x][y]) {
            neighbours.emplace_back(x, y - 1);
        }
    }

    if (!((y + 1) > array[0].size() - 1)) {
        if (array[x][y + 1] == array[x][y]) {
            neighbours.emplace_back(x, y + 1);
        }
    }

    return neighbours;
}

std::vector<std::tuple<int, int>> check_if_set(std::vector<std::vector<int>>& array, int x, int y, std::vector<std::tuple<int, int>>& visited) {
    /* Recursive method to check if the position (x, y) is included in a set. Returns empty list if there isn't a set of numbers */
    std::vector<std::tuple<int, int>> neighbours = check_neighbours(array, x, y);
    for (std::tuple<int, int> i : neighbours) {
        auto it = std::find (visited.begin(), visited.end(), i);
        if (it == visited.end()) {
            visited.emplace_back(std::get<0>(i), std::get<1>(i));
            check_if_set(array, std::get<0>(i), std::get<1>(i), visited);
        }
    }
    return visited;
}

std::vector<std::vector<std::tuple<int, int>>> get_all_sets(std::vector<std::vector<int>> array) {
    /* Method to get all sets of colors in the matrix. This includes empty sets which will are removed in "find_largest_set" */
    std::vector<std::vector<std::tuple<int, int>>> allSets;
    std::vector<std::tuple<int, int>> visited;
    for (int i = 0; i < array.size(); i++) {
        for (int j = 0; j < array[0].size(); j++) {
            visited = {};
            allSets.emplace_back(check_if_set(array, i, j, visited));
        }
    }
    return allSets;
}

std::vector<std::vector<std::tuple<int, int>>> find_largest_set(std::vector<std::vector<int>> array) {
    /* Uses output from "get_all_sets" and finds the largest set of numbers next to each other in the matrix
    if there is multiple sets which are the largest they will all be returned */
    std::vector<std::vector<std::tuple<int, int>>> sets;
    int currentLargestSet = 0;
    for (auto i : get_all_sets(array)) {
        if (i.size() > currentLargestSet) {
            sets = {};
            std::sort (i.begin(), i.end());
            auto it = std::find (sets.begin(), sets.end(), i);
            if (it == sets.end()) {
                sets.emplace_back(i);
                currentLargestSet = i.size();
            }
        } else if (i.size() == currentLargestSet) {
            std::sort (i.begin(), i.end());
            auto it = std::find (sets.begin(), sets.end(), i);
            if (it == sets.end()) {
                sets.emplace_back(i);
            }
        }
    }
    return sets;
}

void pretty_print_array(std::vector<std::vector<int>>& array) {
    /* Print 2D array to the console in a nice way */
    for (int i = 0; i < array.size(); i++) {
        std::cout << "[";
        for (int j = 0; j < array[i].size(); j++) {
            if (j == 0) {
                std::cout << array[i][j];
            } else {
                std::cout << " " << array[i][j];
            }
        }
        std::cout << "]" << std::endl;
    }
    std::cout << std::endl;
}

void pretty_print_find_largest_set_output(std::vector<std::vector<int>>& array, std::vector<std::vector<std::tuple<int, int>>>& numberSet) {
    /* Print output from "find_largest_set" in a nice way thats easy to read and compare coords*/
    for (int i = 0; i < numberSet.size(); i++) {
        std::cout << i + 1 << ". ";
        std::cout << "Number/Color = " << array[std::get<0>(numberSet[i][0])][std::get<1>(numberSet[i][0])] << "\n   Set = [";
        for (int j = 0; j < numberSet[i].size(); j++) {
            if (j + 1 == numberSet[i].size()) {
                std::cout << "(" << std::get<0>(numberSet[i][j]) << ", " << std::get<1>(numberSet[i][j]) << ")";
            } else {
                std::cout << "(" << std::get<0>(numberSet[i][j]) << ", " << std::get<1>(numberSet[i][j]) << "), ";
            }
        }
        std::cout << "]" << std::endl << std::endl;
    }
}
