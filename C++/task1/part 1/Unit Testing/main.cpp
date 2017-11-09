#define CATCH_CONFIG_MAIN
#include "../../../catch.hpp"
#include "../factorial.cpp"

TEST_CASE("Factorials are computed", "[factorial]") {
   REQUIRE(factorial(1) == 1);
   REQUIRE(factorial(2) == 2);
   REQUIRE(factorial(3) == 6);
   REQUIRE(factorial(10) == 3628800);
}

TEST_CASE("Test if factorial(a) % b == 0", "[test_if_divides]") {
   REQUIRE(test_if_divides(6, 9) == 1);
   REQUIRE(test_if_divides(20, 10000) == 1);
   REQUIRE(test_if_divides(6, 27) == 0);
   REQUIRE(test_if_divides(20, 1000000) == 0);
}
