#include <iostream>
#include <string>
#include <map>
#include <vector>
#include "material.hpp"

class lorry {
    public:
        lorry(int ml) {
            maxLoad = ml;
        }

        void set_max_load(int ml);
        void set_load_composition(int lc);
        void set_cargo(std::map<std::string, int> c);

        int get_max_load();
        int get_load_composition();
        std::map<std::string, int> get_cargo();

        int get_cargo_weight();
        int most_expensive_material(std::vector<material> materials);
        void pickup_delivery(std::vector<material> materials);

        friend std::ostream& operator<<(std::ostream& os, lorry& l);

    private:
        int maxLoad;
        int loadComposition = 0;
        std::map<std::string, int> cargo;
};
