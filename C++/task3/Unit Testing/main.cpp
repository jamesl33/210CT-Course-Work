#define CATCH_CONFIG_MAIN
#include "../../catch.hpp"
#include "../cube.hpp"
#include "../stacking.cpp"

TEST_CASE("function should return a pointer to the widest cube in cubeList that isnt in stackedList", "[widest_cube]") {
        cube cube1=cube("red", 5);
        cube cube2=cube("red", 6);
        cube cube3=cube("blue", 5);

        std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
        std::vector<cube*> stackedList = {&cube2};

        REQUIRE(widest_cube(cubeList, stackedList) == &cube3);

        cubeList = {&cube1, &cube2, &cube3};
        stackedList = {};

        REQUIRE(widest_cube(cubeList, stackedList) == &cube2);

        cubeList = {&cube1, &cube2, &cube3};
        stackedList = {&cube2, &cube3};

        REQUIRE(widest_cube(cubeList, stackedList) == &cube1);

        cubeList = {&cube1, &cube2, &cube3};
        stackedList = {&cube1, &cube2, &cube3};

        REQUIRE(widest_cube(cubeList, stackedList) == NULL);
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

TEST_CASE("method to stack cubes according to rules", "[widest_cube]") {
    cube cube1=cube("red", 5);
    cube cube2=cube("red", 6);
    cube cube3=cube("blue", 5);
    cube cube4=cube("purple", 4);
    cube cube5=cube("black", 8);
    cube cube6=cube("black", 4);

    std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
    std::vector<cube*> stackedList = {&cube2, &cube3, &cube1};

    REQUIRE(stack_cubes(cubeList) == stackedList);

    cubeList = {&cube1, &cube2, &cube3, &cube4, &cube5, &cube6};
    stackedList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};

    REQUIRE(stack_cubes(cubeList) == stackedList);

    cubeList = {};
    stackedList = {};

    REQUIRE(stack_cubes(cubeList) == stackedList);

    stackedList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};
    cubeList = {&cube5, &cube2, &cube3, &cube1, &cube4, &cube6};

    REQUIRE(stack_cubes(cubeList) == stackedList);

}
