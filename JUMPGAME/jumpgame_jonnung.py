
class JumpGame:
    def __init__(self, width, game_board):
        self.reachable = False
        self.width = width
        self.game_board = game_board
        self.jump_history = [[0 for _ in range(width)] for _ in range(width)]

    def jump(self, i=0, j=0):
        if self.reachable:
            return True

        if i >= self.width or j >= self.width:
            return False

        if self.jump_history[i][j] != 0:
            return self.jump_history[i][j]

        move_distance = self.game_board[i][j]
        if move_distance == 0:
            self.reachable = True
            return True
        else:
            self.jump_history[i][j] = self.jump(i+move_distance, j) or self.jump(i, j+move_distance)

        return False


if __name__ == '__main__':
    import sys

    rl = lambda: sys.stdin.readline()

    c = int(rl())

    for _ in range(c):
        n = int(rl())
        game_board = []
        for _ in range(n):
            game_board.append(list(map(int, rl().split())))

        jg = JumpGame(n, game_board)
        jg.jump()
        print(jg.jump_history[1][6])
        print("YES" if jg.reachable else "NO")
