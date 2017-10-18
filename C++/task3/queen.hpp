#include <vector>
#include <string>
#include <iostream>

class queen {
    public:
        queen(int bs) {
            boardSize = bs;
        }

        int get_board_size();
        std::vector<int> get_board_state();

        void set_board_size(int bs);
        void set_board_state(std::vector<int> bs);

        bool is_safe(int x, int y);
        std::vector<int> place_queen(int pos);
        void print_vector(std::vector<int> board);

    private:
        int boardSize;
        std::vector<int> boardState;
};

int queen::get_board_size() {
    return boardSize;
}

std::vector<int> queen::get_board_state() {
    return boardState;
}

void queen::set_board_size(int bs) {
    boardSize = bs;
}

void queen::set_board_state(std::vector<int> bs) {
    boardState = bs;
}

bool queen::is_safe(int x, int y) {
    for (int col = 0; col < boardState.size(); col++) {
        int row = get_board_state()[col];
        if (x == col || y == row) {
            return false;
        }
        if (x + y == col + row || x - y == col - row) {
            return false;
        }
    }
    return true;
}

std::vector<int> queen::place_queen(int pos=0) {
    std::vector<int> boardState = get_board_state();
    if (boardState.size() == boardSize) {
        return boardState;
    }
    for (int col = pos; col < boardSize; col++) {
        if (is_safe(boardState.size(), col)) {
            boardState.emplace_back(col);
            set_board_state(boardState);
            return place_queen();
        }
    }
    int lastQueenRow = boardState.back();
    boardState.pop_back();
    set_board_state(boardState);
    return place_queen(lastQueenRow + 1);
}

void queen::print_vector(std::vector<int> board) {
    for (auto i = board.begin(); i != board.end(); i++) {
        if (i == board.begin()) {
            std::cout << "[" << *i << ", ";
        } else if (next(i) == board.end()) {
            std::cout << *i << "]\n";
        } else {
            std::cout << *i << ", ";
        }
    }
}
