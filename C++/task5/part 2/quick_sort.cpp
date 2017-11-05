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
