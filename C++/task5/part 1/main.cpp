#include <vector>
#include <tuple>
#include "set_finding.cpp"

int main() {
    std::vector<std::vector<int>> array = create_array(8, 8); // tested up to (10000, 10000) its takes a little while but does work
    std::vector<std::vector<std::tuple<int, int>>> largestSet = find_largest_set(array);
    pretty_print_array(array);
    pretty_print_find_largest_set_output(array, largestSet);
}
