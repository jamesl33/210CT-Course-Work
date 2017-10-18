#include <vector>
#include <string>
#include <algorithm>
#include "queen.hpp"

// ################# Labsheet main ################# // Comment out code inside of 'Labsheet Main' when running unit test

int main() {
    for (int i = 0; i < 8; i++) {
        queen solver = queen(8);
        std::cout << "Solution " << i + 1 << " - ";
        solver.print_vector(solver.place_queen(i));
    }
}

// ################# Labsheet main #################

// ################# Unit Test ################# // Uncomment code inside of 'Unit Test' when unit testing

//#define CATCH_CONFIG_MAIN
//#include "catch.hpp"
//
//TEST_CASE("Check is its safe to place a queen", "[is_safe]") {
//    queen solver = queen(8);
//    std::vector<int> v = solver.get_board_state();
//    v.emplace_back(0);
//    solver.set_board_state(v);
//
//    REQUIRE((solver.is_safe(0, 1)) == false);
//    REQUIRE((solver.is_safe(1, 0)) == false);
//    REQUIRE((solver.is_safe(1, 1)) == false);
//    REQUIRE((solver.is_safe(2, 1)) == true);
//    REQUIRE((solver.is_safe(1, 2)) == true);
//}
//
//TEST_CASE("Check if place_queen returns correct solution to 8 queens", "[place_queen]") {
//    std::vector<std::vector<int>> knownValues;
//    knownValues = {{0, 4, 7, 5, 2, 6, 1, 3}, {1, 3, 5, 7, 2, 0, 6, 4},
//                   {2, 0, 6, 4, 7, 1, 3, 5}, {3, 0, 4, 7, 1, 6, 2, 5},
//                   {4, 0, 3, 5, 7, 1, 6, 2}, {5, 0, 4, 1, 7, 2, 6, 3},
//                   {6, 0, 2, 7, 5, 3, 1, 4}, {7, 1, 3, 0, 6, 4, 2, 5}};
//
//    for (int i = 0; i < 8; i++) {
//        queen solver = queen(8);
//        std::vector<int> proposedSolution = solver.place_queen(i);
//        REQUIRE(std::find(knownValues.begin(), knownValues.end(), proposedSolution) != knownValues.end());
//    }
//}

// ################# Unit Test #################
