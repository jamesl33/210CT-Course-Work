#include <string>

class material {
	public:
		material(std::string nme, int qty, int price_per_kilo) {
			name = nme;
			quantity = qty;
			ppk = price_per_kilo;
		}

		void set_name(std::string nme);
		void set_quantity(int qty);
		void set_price_per_kilo(int price);

		std::string get_name();
		int get_quantity();
		int get_price_per_kilo();

		void decriment();
	
	private:
		std::string name;
		int quantity;
		int ppk;
};

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
