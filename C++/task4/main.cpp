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

cube* wideset_cube(std::vector<cube*>& cubeList, std::vector<cube*>& stackedList) {
    int widest;
    cube* widesetCube = nullptr;
    cube* last = nullptr;

    if (!stackedList.empty()) {
        last = stackedList.back();
    }

    for (cube* i: cubeList) {
        if (!(std::find(stackedList.begin(), stackedList.end(), i) != stackedList.end())) {
            if (i -> get_edge_length() > widest && i -> get_color() != last -> get_color()) {
                widesetCube = i;
            }
        }
    }

    return widesetCube;
}

std::string stack_cubes(std::vector<cube*> cubeList) {

}

// ################# Labsheet main ################# // Comment out code inside of 'Labsheet Main' when running unit test

// ################# Labsheet main #################

// ################# Unit Test ################# // Uncomment code inside of 'Unit Test' when unit testing

#define CATCH_CONFIG_MAIN
#include "../catch.hpp"

TEST_CASE("function should return a pointer to the widest cube in cubeList that isnt in stackedList", "[wideset_cube]") {
        cube cube1=cube("red", 5);
        cube cube2=cube("red", 6);
        cube cube3=cube("blue", 5);

        std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
        std::vector<cube*> stackedList = {&cube2};

        REQUIRE(wideset_cube(cubeList, stackedList) == &cube3);

        cubeList = {&cube1, &cube2, &cube3};
        stackedList = {&cube1, &cube2, &cube3};

        REQUIRE(wideset_cube(cubeList, stackedList) == NULL);

        cubeList = {&cube1, &cube2, &cube3};
        stackedList = {&cube2, &cube3};

        REQUIRE(wideset_cube(cubeList, stackedList) == &cube1);
}

TEST_CASE("function should return total height of 'stackedList' of cubes", "[calculate_height]") {
    cube cube1=cube("red", 5);
    cube cube2=cube("red", 6);
    cube cube3=cube("blue", 5);

    std::vector<cube*> stackedList = {&cube2};

    REQUIRE(calculate_height(stackedList) == 6);

    stackedList = {&cube1, &cube2, &cube3};

    REQUIRE(calculate_height(stackedList) == 16);

    stackedList = {&cube2, &cube3};

    REQUIRE(calculate_height(stackedList) == 11);

    REQUIRE(calculate_height({}) == 0);


}

// ################# Unit Test #################
