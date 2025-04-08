def is_solved(board):
    res = 0
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 0:
                res = -1
                continue
            if j == 0:
                if row[j+1] == cell and row[j+2] == cell:
                    return cell
            if i == 0:
                if board[i+1][j] == cell and board[i+2][j] == cell:
                    return cell
            if i == 0 and j == 0:
                if board[i+1][j+1] == cell and board[i+2][j+2] == cell:
                    return cell
            if i == 0 and j == 2:
                if board[i+1][j-1] == cell and board[i+2][j-2] == cell:
                    return cell
    return res
## Cleanest solution seen on code wars :
def is_solved(board):
    bb = ''.join([str(x) for y in board for x in y])
    winning_stage = [
        bb[:3], bb[3:6] , bb[6:],
        bb[:7:3], bb[1:8:3], bb[2::3],
        bb[::4], bb[2:7:2]
    ]
    if '111' in winning_stage:
        return 1
    elif '222' in winning_stage:
        return 2
    else:
        if '0' in bb:
            return -1
        else:
            return 0