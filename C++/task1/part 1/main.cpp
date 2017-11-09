#include "factorial.cpp"

int main() {
		test_if_divides(6, 9);
		test_if_divides(20, 10000);
		test_if_divides(6, 27);
		test_if_divides(20, 1000000);
}

// ################# Pseudo Code #################

// FACTORIAL(n)
//  IF n = 0
//      RETURN 1
//  ELSE
//      RETURN n * FACTORIAL(n - 1)

// TEST-IF-DEVIDES(a, b)
//  IF a! MOD b = 0
//      RETURN true
//  ELSE
//      RETURN false

// ################# Pseudo Code #################
