#include <iostream>
#include <string>
#include <vector>
#include "material.hpp"
#include "lorry.hpp"

// ################# Labsheet main ################# // Uncomment code inside of 'Labsheet main' when not running unit testing

// int main() {
// 	material gold=material("Gold", 4, 100);
// 	material copper=material("Copper", 7, 65);
// 	material plastic=material("Plastic", 15, 50);
// 	std::vector<material> materials_labsheet = {gold, plastic, copper};

// 	lorry lorry1=lorry(10);
// 	lorry1.pickup_delivery(materials_labsheet);
// 	std::cout << lorry1 << std::endl;
// } 

// ################# Labsheet main #################

// ################# Unit Test ################# // Comment out code inside of 'Unit Test' when not unit testing

#define CATCH_CONFIG_MAIN
#include "catch.hpp"

TEST_CASE("Most expensive load is calculated", "[lorry]") {
	// create all the material objects
	material gold=material("Gold", 4, 100);
	material copper=material("Copper", 7, 65);
	material plastic=material("Plastic", 15, 50);
	material diamond=material("Diamond", 1, 1000);
	material ruby=material("Ruby", 2, 500);

	std::vector<material> materials_labsheet = {gold, plastic, copper};
	std::vector<material> materials_extra = {gold, plastic, copper, diamond, ruby};

	std::map<std::string, int> know_values_labsheet = {{"Gold", 4}, {"Copper", 6}};
	std::map<std::string, int> know_values_extra = {{"Diamond", 1}, {"Ruby", 2}, {"Gold", 4}, {"Copper", 7}, {"Plastic", 1}};

	lorry lorry1=lorry(10);
	lorry1.pickup_delivery(materials_labsheet);
	std::cout << lorry1 << std::endl << std::endl;

	lorry lorry2=lorry(15);
	lorry2.pickup_delivery(materials_extra);
	std::cout << lorry2 << std::endl << std::endl;

	REQUIRE(lorry1.get_cargo() == know_values_labsheet);
	REQUIRE(lorry2.get_cargo() == know_values_extra);
}

// ################# Unit Test #################
