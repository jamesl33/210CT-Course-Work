#include <iostream>
#include <vector>

// Hoare partition scheme quick sort
// https://en.wikipedia.org/wiki/Quicksort

int partition(std::vector<int>& unsorted, int low, int high) {
    int pivot = unsorted[low];
    int i = low - 1;
    int j = high + 1;

    while (true) {
        do {
            i++;
        }
        while (unsorted[i] < pivot);
        do {
            j--;
        }
        while (unsorted[j] > pivot);

        if (i >= j) {
            return j;
        }

        std::swap(unsorted[i], unsorted[j]);
    }
}

void quick_sort(std::vector<int>& unsorted, int low, int high)
{
    if (low < high) {
        int p = partition(unsorted, low, high);
        quick_sort(unsorted, low, p);
        quick_sort(unsorted, p + 1, high);
    }
}

// ################# Labsheet main ################# // Comment out code inside of 'Labsheet Main' when running unit test

int main() {

}

// ################# Labsheet main #################

// ################# Unit Test ################# // Uncomment code inside of 'Unit Test' when unit testing

// #define CATCH_CONFIG_MAIN
// #include "../catch.hpp"
// #include <algorithm>

// TEST_CASE("function to sort vector", "[quick_sort]") {
//     std::vector<int> a;
//     std::vector<int> b;

//     SECTION("already sorted vector") {
//         a = {1, 2, 3, 4, 5};
//         b = {1, 2, 3, 4, 5};

//         quick_sort(a, 0, a.size() - 1);

//         REQUIRE(a == b);
//     }

//     SECTION("unsorted vector") {
//         a = {1, 5, 2, 3, 4};
//         b = {1, 2, 3, 4, 5};

//         quick_sort(a, 0, a.size() - 1);

//         REQUIRE(a == b);
//     }

//     SECTION("very large vector") {
//         for(int i = 0; i < 10000; i++)
//         {
//             int num = rand() % 1000;
//             a.emplace_back(num);
//             b.emplace_back(num);
//         }

//         std::sort(b.begin(), b.end()); // sort using standard library
//         quick_sort(a, 0, a.size() - 1); // sort using 'quick_sort'

//         REQUIRE(a == b);
//     }
// }

// ################# Unit Test #################
