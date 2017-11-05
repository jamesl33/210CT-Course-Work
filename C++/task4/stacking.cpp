#include <vector>
#include <algorithm>

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

    for (cube* i : cubeList) {
        if (!(std::find(stackedList.begin(), stackedList.end(), i) != stackedList.end())) {
            if (stackedList.empty())
            {
                if (i -> get_edge_length() > widest) {
                    widest = i -> get_edge_length();
                    widestCube = i;
                }
            }
            else
            {
                last = stackedList.back();
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
