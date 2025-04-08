package kata

func IsSolved(board [3][3]int) int {
	res := 0
	for i, row := range board {
		for j, cell := range row {
			if cell == 0 {
				res = -1
				continue
			}
			if j == 0 {
				if row[j+1] == cell && row[j+2] == cell {
					return cell
				}
			}
			if i == 0 {
				if board[i+1][j] == cell && board[i+2][j] == cell {
					return cell
				}
			}
			if i == 0 && j == 0 {
				if board[i+1][j+1] == cell && board[i+2][j+2] == cell {
					return cell
				}
			}
			if i == 0 && j == 2 {
				if board[i+1][j-1] == cell && board[i+2][j-2] == cell {
					return cell
				}
			}
		}
	}
	return res
}
