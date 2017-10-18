#include <vector>
#include <string>
#include <iostream>

class queen {
	public:
		queen(int bs) {
			boardSize = bs;
		}

		int boardSize;
		std::vector<int> boardState;

		bool is_safe(int x, int y);
		std::vector<int> place_queen(int pos);
		void print_vector(std::vector<int> board);
};

bool queen::is_safe(int x, int y) {
	for (int col = 0; col < boardState.size(); col++) {
		int row = boardState[col];
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
	if (boardState.size() == boardSize) {
		return boardState;
	}
	for (int col = pos; col < boardSize; col++) {
		if (is_safe(boardState.size(), col)) {
			boardState.emplace_back(col);
			return place_queen();
		}
	}
	int lastQueenRow = boardState.back();
	boardState.pop_back();
	return place_queen(lastQueenRow + 1);
}

void queen::print_vector(std::vector<int> board) {
	for (auto i = board.begin(); i != board.end(); i++) {
		if (i == board.begin()) {
			std::cout << "[";
		} else if (next(i) == board.end()) {
			std::cout << *i << "]\n";
		} else {
			std::cout << *i << ", ";
		}
	}
}
