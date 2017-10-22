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
