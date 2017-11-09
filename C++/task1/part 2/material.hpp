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
