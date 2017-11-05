#include <iostream>
#include "queen.hpp"

int main() {
		for (int i = 0; i < 8; i++) {
				queen solver = queen(8);
				std::cout << "Solution " << i + 1 << " - ";
				solver.print_vector(solver.place_queen(i));
		}
}
