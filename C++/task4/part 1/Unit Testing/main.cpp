#define CATCH_CONFIG_MAIN
#include "../../../catch.hpp"
#include "../set_finding.cpp"

TEST_CASE("function to check neighbours of array 'x,y' position", "[check_neighbours]") {
    std::vector<std::vector<int>> array;

    SECTION("left") {
        array = {{0, 0, 0, 0}, {1, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        std::vector<std::tuple<int, int>> correct = {{1, 0}};
        REQUIRE(check_neighbours(array, 1, 1) == correct);
    }

    SECTION("right") {
        array = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        std::vector<std::tuple<int, int>> correct = {{1, 2}};
        REQUIRE(check_neighbours(array, 1, 1) == correct);
    }

    SECTION("above") {
        array = {{0, 1, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        std::vector<std::tuple<int, int>> correct = {{0, 1}};
        REQUIRE(check_neighbours(array, 1, 1) == correct);
    }

    SECTION("below") {
        array = {{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}};
        std::vector<std::tuple<int, int>> correct = {{2, 1}};
        REQUIRE(check_neighbours(array, 1, 1) == correct);
    }
}

TEST_CASE("function to check if there is a set of numbers in a matrix/array", "[check_if_set]") {
    std::vector<std::vector<int>> array;
    std::vector<std::tuple<int, int>> visited;

    SECTION("set of 5 numbers") {
        array = {{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}};
        visited = {};

        std::vector<std::tuple<int, int>> correct = {{ 0, 1 }, { 1, 0 }, { 1, 1 }, { 1, 2 }, { 2, 1 }};
        std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
        std::sort (returnedValue.begin(), returnedValue.end());

        REQUIRE(returnedValue == correct);
    }

    SECTION("set of 2 numbers") {
        array = {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        visited = {};

        std::vector<std::tuple<int, int>> correct = {{1, 1}, {1, 2}};
        std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
        std::sort (returnedValue.begin(), returnedValue.end());

        REQUIRE(returnedValue == correct);
    }

    SECTION("set of 16 numbers") {
        array = {{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}};
        visited = {};

        std::vector<std::tuple<int, int>> correct = {{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 0}, {1, 1}, {1, 2}, {1, 3}, {2, 0}, {2, 1}, {2, 2}, {2, 3}, {3, 0}, {3, 1}, {3, 2}, {3, 3}};
        std::vector<std::tuple<int, int>> returnedValue = check_if_set(array, 1, 1, visited);
        std::sort (returnedValue.begin(), returnedValue.end());

        REQUIRE(returnedValue == correct);
    }
}

TEST_CASE("find the largest set of numbers in an array", "[find_largest_set]") {
    std::vector<std::vector<int>> array;
    std::vector<std::vector<std::tuple<int, int>>> correct;

    SECTION("set of 16 numbers") {
        array = {{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}};
        correct = {{{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 0}, {1, 1}, {1, 2}, {1, 3}, {2, 0}, {2, 1}, {2, 2}, {2, 3}, {3, 0}, {3, 1}, {3, 2}, {3, 3}}};

        REQUIRE(find_largest_set(array) == correct);
    }
}
