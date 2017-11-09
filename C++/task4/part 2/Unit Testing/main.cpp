#include <algorithm>
#define CATCH_CONFIG_MAIN
#include "../../../catch.hpp"
#include "../quick_sort.cpp"

TEST_CASE("function to sort vector", "[quick_sort]") {
    std::vector<int> a;
    std::vector<int> b;

    SECTION("already sorted vector") {
        a = {1, 2, 3, 4, 5};
        b = {1, 2, 3, 4, 5};

        quick_sort(a, 0, a.size() - 1);

        REQUIRE(a == b);
    }

    SECTION("unsorted vector") {
        a = {1, 5, 2, 3, 4};
        b = {1, 2, 3, 4, 5};

        quick_sort(a, 0, a.size() - 1);

        REQUIRE(a == b);
    }

    SECTION("very large vector") {
        for(int i = 0; i < 10000; i++)
        {
            int num = rand() % 1000;
            a.emplace_back(num);
            b.emplace_back(num);
        }

        std::sort(b.begin(), b.end()); // sort using standard library
        quick_sort(a, 0, a.size() - 1); // sort using 'quick_sort'

        REQUIRE(a == b);
    }
}
