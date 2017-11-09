#include <iostream>
#include <vector>
#include "cube.hpp"
#include "stacking.cpp"

int main() {
    cube cube1=cube("red", 5);
    cube cube2=cube("red", 6);
    cube cube3=cube("blue", 5);

    std::vector<cube*> cubeList = {&cube1, &cube2, &cube3};
    std::cout << "The maximum height is " << calculate_height(stack_cubes(cubeList)) << std::endl;
}
