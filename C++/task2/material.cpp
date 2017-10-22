#include "material.hpp"

void material::set_name(std::string nme) {
		name = nme;
}

void material::set_quantity(int qty) {
		quantity = qty;
}

void material::set_price_per_kilo(int price) {
		ppk = price;
}

std::string material::get_name() {
		return name;
}

int material::get_quantity() {
		return quantity;
}

int material::get_price_per_kilo() {
		return ppk;
}

void material::decriment() {
		quantity--;
}
