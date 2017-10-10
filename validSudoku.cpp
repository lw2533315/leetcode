// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

// The Sudoku board could be partially filled, where empty cells are filled with the character '.'.



#include<bits/stdc++.h>

using namespace std;
class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		set <char> s;

		//check row
		for(int i = 0 ; i < board.size(); i ++) {
			s.clear();
			for ( int j = 0 ; j< board.size(); j++) {
				if (board[i][j] != '.' and s.insert(board[i][j]).second==false) {

					return false;
				}
			}
		}

		//check colum
		for(int i = 0 ; i < board.size(); i ++) {
			s.clear();
			for ( int j = 0 ; j< board.size(); j++) {
				if (board[j][i] != '.' and !s.insert(board[j][i]).second) {

					return false;
				}
			}
		}

		//check block
		for(int i = 0 ; i < board.size(); i ++) {
			s.clear();
			for ( int j = 0 ; j< board.size(); j++) {
				if (board[3*(i/3) + j/3][ 3*(i%3) + j%3] != '.' and !s.insert(board[3*(i/3) + j/3][ 3*(i%3) + j%3]).second) {

					return false;
				}
			}
		}

		return true;
	}

};


int main() {
	return 0;
}