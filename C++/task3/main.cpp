#include <vector>
#include <string>
#include <algorithm>
#include "queen.hpp"

// ################# Labsheet main ################# // Uncomment code inside of 'Labsheet main' when not running unit testing

int main() {
	queen solver = queen(8);
	solver.print_vector(solver.place_queen());
}

// ################# Labsheet main #################

// ################# Unit Test ################# // Comment out code inside of 'Unit Test' when not unit testing

// #define CATCH_CONFIG_MAIN
// #include "catch.hpp"

// TEST_CASE("Check is its safe to place a queen", "[is_safe]") {
// 	queen solver = queen(8);
// 	solver.boardState.emplace_back(0);
// 	REQUIRE((solver.is_safe(0, 1)) == false);
// 	REQUIRE((solver.is_safe(1, 0)) == false);
// 	REQUIRE((solver.is_safe(1, 1)) == false);
// 	REQUIRE((solver.is_safe(2, 1)) == true);
// 	REQUIRE((solver.is_safe(1, 2)) == true);
// }

// TEST_CASE("Check if place_queen returns correct solution to 8 queens", "[place_queen]") {
// 	queen solver = queen(8);
// 	std::vector<int> knowCorrectValues = {0, 4, 7, 5, 2, 6, 1, 3};
// 	REQUIRE(solver.place_queen() == knowCorrectValues);
// }

// ################# Unit Test #################