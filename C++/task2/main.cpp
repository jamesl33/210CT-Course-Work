#define CATCH_CONFIG_MAIN
#include <iostream>
#include <string>
#include <vector>
#include "catch.h"
#include "material.h"
#include "lorry.h"

// ################# Unit Test #################

TEST_CASE("Most expensive load is calculated", "[lorry]")
{
	material gold=material();
	gold.set_name("Gold");
	gold.set_quantity(4);
	gold.set_price_per_kilo(100);

	material copper=material();
	copper.set_name("Copper");
	copper.set_quantity(7);
	copper.set_price_per_kilo(65);

	material plastic=material();
	plastic.set_name("Plastic");
	plastic.set_quantity(15);
	plastic.set_price_per_kilo(50);

	material diamond=material();
	diamond.set_name("Diamond");
	diamond.set_quantity(1);
	diamond.set_price_per_kilo(1000);

	material ruby=material();
	ruby.set_name("Ruby");
	ruby.set_quantity(2);
	ruby.set_price_per_kilo(500);

	std::vector<material> materials_labsheet = {gold, plastic, copper};
	std::vector<material> materials_extra = {gold, plastic, copper, diamond, ruby};

	std::map<std::string, int> know_values_labsheet = {{"Gold", 4}, {"Copper", 6}};
	std::map<std::string, int> know_values_extra = {{"Diamond", 1}, {"Ruby", 2}, {"Gold", 4}, {"Copper", 7}, {"Plastic", 1}};

	lorry lorry1=lorry();
	lorry1.set_max_load(10);
	lorry1.pickup_delivery(materials_labsheet);

	REQUIRE(lorry1.get_cargo() == know_values_labsheet);

	lorry lorry2=lorry();
	lorry2.set_max_load(15);
	lorry2.pickup_delivery(materials_extra);

	REQUIRE(lorry2.get_cargo() == know_values_extra);

}

// ################# Unit Test #################