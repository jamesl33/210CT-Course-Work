#include <vector>
#include <tuple>
#include <algorithm>
#include <iostream>

std::vector<std::vector<int>> create_array(int n, int m) {
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

// ################# Labsheet main ################# // Comment out code inside of 'Labsheet Main' when running unit test

int main() {
    std::vector<std::vector<int>> array = create_array(8, 8); // tested up to (10000, 10000) its takes a little while but does work
    std::vector<std::vector<std::tuple<int, int>>> largestSet = find_largest_set(array);
    pretty_print_array(array);
    pretty_print_find_largest_set_output(array, largestSet);
}

// ################# Labsheet main #################

// ################# Unit Test ################# // Uncomment code inside of 'Unit Test' when unit testing

// #define CATCH_CONFIG_MAIN
// #include "../../catch.hpp"

// TEST_CASE("function to check neighbours of array 'x,y' position", "[check_neighbours]") {
//     std::vector<std::vector<int>> array;

//     SECTION("left") {
//         array = {{0, 0, 0, 0}, {1, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
//         std::vector<std::tuple<int, int>> correct = {{1, 0}};
//         REQUIRE(check_neighbours(array, 1, 1) == correct);
//     }

//     SECTION("right") {
//         array = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
//         std::vector<std::tuple<int, int>> correct = {{1, 2}};
//         REQUIRE(check_neighbours(array, 1, 1) == correct);
//     }

//     SECTION("above") {
//         array = {{0, 1, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
//         std::vector<std::tuple<int, int>> correct = {{0, 1}};
//         REQUIRE(check_neighbours(array, 1, 1) == correct);
//     }

//     SECTION("below") {
//         array = {{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}};
//         std::vector<std::tuple<int, int>> correct = {{2, 1}};
//         REQUIRE(check_neighbours(array, 1, 1) == correct);
//     }
// }

// TEST_CASE("function to check if there is a set of numbers in a matrix/array", "[check_if_set]") {
//     std::vector<std::vector<int>> array;
//     std::vector<std::tuple<int, int>> visited;

//     SECTION("set of 5 numbers") {
//         array = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}};
//         visited = {};

//         std::vector<std::tuple<int, int>> correct = {{ 0, 1 }, { 1, 0 }, { 1, 1 }, { 1, 2 }, { 2, 1 }};
//         std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
//         std::sort (returnedValue.begin(), returnedValue.end());

//         REQUIRE(returnedValue == correct);
//     }

//     SECTION("set of 2 numbers") {
//         array = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
//         visited = {};

//         std::vector<std::tuple<int, int>> correct = {{1, 1}, {1, 2}};
//         std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
//         std::sort (returnedValue.begin(), returnedValue.end());

//         REQUIRE(returnedValue == correct);
//     }

//     SECTION("set of 16 numbers") {
//         array = {{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}};
//         visited = {};

//         std::vector<std::tuple<int, int>> correct = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 0}, {1, 1}, {1, 2}, {1, 3}, {2, 0}, {2, 1}, {2, 2}, {2, 3}, {3, 0}, {3, 1}, {3, 2}, {3, 3}};
//         std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
//         std::sort (returnedValue.begin(), returnedValue.end());

//         REQUIRE(returnedValue == correct);
//     }
// }

// TEST_CASE("find the largest set of numbers in an array", "[find_largest_set]") {
//     std::vector<std::vector<int>> array;
//     std::vector<std::vector<std::tuple<int, int>>> correct;

//     SECTION("set of 16 numbers") {
//         array = {{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}};
//         correct = {{{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 0}, {1, 1}, {1, 2}, {1, 3}, {2, 0}, {2, 1}, {2, 2}, {2, 3}, {3, 0}, {3, 1}, {3, 2}, {3, 3}}};

//         REQUIRE(find_largest_set(array) == correct);
//     }
// }

// ################# Unit Test #################
