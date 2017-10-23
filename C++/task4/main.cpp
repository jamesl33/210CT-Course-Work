#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "cube.hpp"

int calculate_height(std::vector<cube*> stackedList) {
    int height = 0;
    for (auto i : stackedList) {
        height += i -> get_edge_length();
    }

    return height;
}

cube* widest_cube(std::vector<cube*>& cubeList, std::vector<cube*>& stackedList) {
    int widest = 0;
    cube* widestCube = nullptr;
    cube* last = nullptr;

    if (stackedList.empty()) {
        for (cube* i : cubeList) {
            if (!(std::find(stackedList.begin(), stackedList.end(), i) != stackedList.end())) {
                if (i -> get_edge_length() > widest) {
                    widest = i -> get_edge_length();
                    widestCube = i;
                }
            }
        }
    } else {
        last = stackedList.back();
        for (cube* i : cubeList) {
            if (!(std::find(stackedList.begin(), stackedList.end(), i) != stackedList.end())) {
                if (i -> get_edge_length() > widest && i -> get_color() != last -> get_color()) {
                    widest = i -> get_edge_length();
                    widestCube = i;
                }
            }
        }
    }

    return widestCube;
}

std::vector<cube*> stack_cubes(std::vector<cube*>& cubeList) {
    if (cubeList.size() <= 0) {
        return {};
    }

    std::vector<cube*> stackedList;
    stackedList.emplace_back(widest_cube(cubeList, stackedList));

    while (stackedList.size() != cubeList.size()) {
        stackedList.emplace_back(widest_cube(cubeList, stackedList));
    }

    return stackedList;
}

// ################# Labsheet main ################# // Comment out code inside of 'Labsheet Main' when running unit test

int main() {
    cube cube1=cube("red", 5);
    cube cube2=cube("red", 6);
    cube cube3=cube("blue", 5);

    std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
    std::cout << "The maximum height is " << calculate_height(stack_cubes(cubeList)) << std::endl;
}

// ################# Labsheet main #################

// ################# Unit Test ################# // Uncomment code inside of 'Unit Test' when unit testing

// #define CATCH_CONFIG_MAIN
// #include "../catch.hpp"

// TEST_CASE("function should return a pointer to the widest cube in cubeList that isnt in stackedList", "[widest_cube]") {
//         cube cube1=cube("red", 5);
//         cube cube2=cube("red", 6);
//         cube cube3=cube("blue", 5);

//         std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
//         std::vector<cube*> stackedList = {&cube2};

//         REQUIRE(widest_cube(cubeList, stackedList) == &cube3);

//         cubeList = {&cube1, &cube2, &cube3};
//         stackedList = {};

//         REQUIRE(widest_cube(cubeList, stackedList) == &cube2);

//         cubeList = {&cube1, &cube2, &cube3};
//         stackedList = {&cube2, &cube3};

//         REQUIRE(widest_cube(cubeList, stackedList) == &cube1);

//         cubeList = {&cube1, &cube2, &cube3};
//         stackedList = {&cube1, &cube2, &cube3};

//         REQUIRE(widest_cube(cubeList, stackedList) == NULL);
// }

// TEST_CASE("function should return total height of 'stackedList' of cubes", "[calculate_height]") {
//     cube cube1=cube("red", 5);
//     cube cube2=cube("red", 6);
//     cube cube3=cube("blue", 5);

//     std::vector<cube*> stackedList = {&cube2};

//     REQUIRE(calculate_height(stackedList) == 6);

//     stackedList = {&cube1, &cube2, &cube3};

//     REQUIRE(calculate_height(stackedList) == 16);

//     stackedList = {&cube2, &cube3};

//     REQUIRE(calculate_height(stackedList) == 11);

//     REQUIRE(calculate_height({}) == 0);
// }

// TEST_CASE("method to stack cubes according to rules", "[widest_cube]") {
//     cube cube1=cube("red", 5);
//     cube cube2=cube("red", 6);
//     cube cube3=cube("blue", 5);
//     cube cube4=cube("purple", 4);
//     cube cube5=cube("black", 8);
//     cube cube6=cube("black", 4);

//     std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
//     std::vector<cube*> stackedList = {&cube2, &cube3, &cube1};

//     REQUIRE(stack_cubes(cubeList) == stackedList);

//     cubeList = {&cube1, &cube2, &cube3, &cube4, &cube5, &cube6};
//     stackedList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};

//     REQUIRE(stack_cubes(cubeList) == stackedList);

//     cubeList = {};
//     stackedList = {};

//     REQUIRE(stack_cubes(cubeList) == stackedList);

//     stackedList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};
//     cubeList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};

//     REQUIRE(stack_cubes(cubeList) == stackedList);

// }

// ################# Unit Test #################
