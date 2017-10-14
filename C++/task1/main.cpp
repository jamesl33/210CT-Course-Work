#include <iostream>
#define CATCH_CONFIG_MAIN
#include "catch.h"

long factorial(long n) {
	if (n == 0) {
		return 1;
	} else {
		return n * factorial(n - 1);
	}
}

bool test_if_divides(int a, int b) {
	if (factorial(a) % b) {
		std::cout << b << " does not divide by " << a << "!" << std::endl;
		return false;
	} else {
		std::cout << b << " does divide by " << a << "!" << std::endl;
		return true;
	}
}

// ################# Pseudo Code #################

// FACTORIAL(n)
// 	IF n = 0
// 		RETURN 1
// 	ELSE
// 		RETURN n * FACTORIAL(n - 1)

// TEST-IF-DEVIDES(a, b)
// 	IF a! MOD b = 0
// 		RETURN true
// 	ELSE
// 		RETURN false

// ################# Pseudo Code #################

// ################# Unit Test #################

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

// ################# Unit Test #################