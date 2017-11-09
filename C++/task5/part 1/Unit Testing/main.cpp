#define CATCH_CONFIG_MAIN
#include "../../../catch.hpp"
#include "../diagonals.cpp"

TEST_CASE("function to get the diagonal values in a matrix", "[get_diagonal]") {
    std::vector<std::vector<int>> array;
    std::vector<int> correct;

    SECTION("offset - 1") {
        correct = {1, 1, 1};
        array = {{0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}, {0, 0, 0, 0}};
        REQUIRE(get_diagonal(array, -1) == correct);
    }
    SECTION("offset - 2") {
        correct = {1, 1};
        array = {{0, 0, 1, 0}, {0, 0, 0, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        REQUIRE(get_diagonal(array, -2) == correct);
    }
    SECTION("offset - 3") {
        correct = {1};
        array = {{0, 0, 0, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
        REQUIRE(get_diagonal(array, -3) == correct);
    }
    SECTION("main diagonal") {
        correct = {1, 1, 1, 1};
        array = {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
        REQUIRE(get_diagonal(array) == correct);
    }
    SECTION("offset + 1") {
        correct = {1, 1, 1};
        array = {{0, 0, 0, 0}, {1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}};
        REQUIRE(get_diagonal(array, 1) == correct);
    }
    SECTION("offset + 2") {
        correct = {1, 1};
        array = {{0, 0, 0, 0}, {0, 0, 0, 0}, {1, 0, 0, 0}, {0, 1, 0, 0}};
        REQUIRE(get_diagonal(array, 2) == correct);
    }
    SECTION("offset + 3") {
        correct = {1};
        array = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {1, 0, 0, 0}};
        REQUIRE(get_diagonal(array, 3) == correct);
    }
}

TEST_CASE("function to get all diagonals that are parallel to the main diagonal", "[get_all_diagonals]") {
    std::vector<std::vector<int>> array;
    std::vector<std::vector<int>> correct;

    SECTION("only main diagonal") {
        correct = {{0, 0}, {0, 0, 0}, {1, 1, 1, 1}, {0, 0, 0}, {0, 0}};
        array = {{1, 0, 0, 0}, {0, 1, 0, 0}, {0, 0, 1, 0}, {0, 0, 0, 1}};
        REQUIRE(get_all_diagonals(array, 2) == correct);
    }
}

TEST_CASE("function to test vector slicing", "[vector_slice]") {
    std::vector<int> array;
    std::vector<int> correct;

    SECTION("0 to 3") {
        array = {0, 1, 4, 6, 2};
        correct = {0, 1, 4};
        REQUIRE(vector_slice(array, 0, 3) == correct);
    }
    SECTION("0 to 3") {
        array = {0, 1, 4, 6, 2};
        correct = {6, 2};
        REQUIRE(vector_slice(array, 3, 5) == correct);
    }
}

TEST_CASE("function to find the smallest some of 'n' integers in array", "[smallest_sum_in_array]") {
    std::vector<int> array;

    SECTION("4") {
        array = {0, 1, 4, 6, 2, 0, 4, 7, 3};
        REQUIRE(smallest_sum_in_array(array, 4) == 3);
    }
    SECTION("8") {
        array = {0, 1, 4, 6, 2, 0, 4, 7, 3};
        REQUIRE(smallest_sum_in_array(array, 8) == 20);
    }
}
