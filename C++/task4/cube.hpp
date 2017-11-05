#include <string>

class cube {
    public:
        cube(std::string c, int el) {
            color = c;
            edgeLength = el;
        }

        std::string get_color();
        int get_edge_length();
    private:
        std::string color;
        int edgeLength;
};
