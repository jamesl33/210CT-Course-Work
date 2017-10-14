#include <string>
#include <map>
#include <vector>

class lorry
{
	public:
		// setters
		void set_max_load(int ml);
		void set_load_composition(int lc);
		void set_cargo(std::map<std::string, int> c);
		// getters
		int get_max_load();
		int get_load_composition();
		std::map<std::string, int> get_cargo();
		// functions
		int get_cargo_weight();
		int most_expensive_material(std::vector<material> materials);
		void pickup_delivery(std::vector<material> materials);

	private:
		int maxLoad;
		int loadComposition = 0;
		std::map<std::string, int> cargo;
};

void lorry::set_max_load(int ml) 
{
	maxLoad = ml;
}

void lorry::set_load_composition(int lc) 
{
	loadComposition = lc;
}
void lorry::set_cargo(std::map<std::string, int> c) 
{
	cargo = c;
}
int lorry::get_max_load() 
{
	return maxLoad;
}
int lorry::get_load_composition() 
{
	return loadComposition;
}
std::map<std::string, int> lorry::get_cargo() 
{
	return cargo;
}

int lorry::get_cargo_weight()
{
	int weight = 0;
	for (auto const& material : this -> get_cargo())
	{
		weight += material.second;	
	}
	return weight;
}

int lorry::most_expensive_material(std::vector<material> materials)
{
	int cost = 0;
	int most_expensive = 0;
	for(int i = 0; i < materials.size(); i++)
	{
		if (materials[i].get_price_per_kilo() > cost and materials[i].get_quantity() > 0)
		{
			cost = materials[i].get_price_per_kilo();
			most_expensive = i;
		}
	}
	return most_expensive;
}

void lorry::pickup_delivery(std::vector<material> materials)
{
	int lc = 0;
	int most_expensive_index = 0;
	std::map<std::string, int> cargo;

	while(this -> get_cargo_weight() < this -> get_max_load())
	{
		most_expensive_index = this -> most_expensive_material(materials);
		cargo = this -> get_cargo();
		
		if(cargo.find(materials[most_expensive_index].get_name()) == cargo.end())
		{
			cargo[(materials[most_expensive_index].get_name())] = 1;
			lc += materials[most_expensive_index].get_price_per_kilo();
			this -> set_cargo(cargo);
			this -> set_load_composition(lc);
		}
		else
		{
			cargo[(materials[most_expensive_index].get_name())] += 1;
			lc += materials[most_expensive_index].get_price_per_kilo();
			this -> set_cargo(cargo);
			this -> set_load_composition(lc);
		}
		materials[most_expensive_index].decriment();
	}
}