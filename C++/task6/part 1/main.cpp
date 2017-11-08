#include <iostream>
#include <vector>
#include "diagonals.cpp"

int main() {
    int n = 4;
    int m = 2;

    if (m > n) {
        std::cout << "'m' is larger than the size of the array" << std::endl;
        std::exit(0);
    }
    else {
        std::vector<int> sumInDiagonals;
        std::vector<std::vector<int>> array = create_array(4);
        std::vector<std::vector<int>> diagonals = get_all_diagonals(array, m);

        for (auto i : diagonals) {
            sumInDiagonals.emplace_back(smallest_sum_in_array(i, m));
        }

        pretty_print_array(array);
        std::cout << std::endl;
        std::cout << "Answer: " << get_min(sumInDiagonals) << std::endl;
    }
}
