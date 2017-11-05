#include <iostream>
#include "lorry.hpp"

int main() {
		material gold=material("Gold", 4, 100);
		material copper=material("Copper", 7, 65);
		material plastic=material("Plastic", 15, 50);
		std::vector<material> materials_labsheet = {gold, plastic, copper};

		lorry lorry1=lorry(10);
		lorry1.pickup_delivery(materials_labsheet);
		std::cout << lorry1 << std::endl;
}
