for row in range(COLUMN_COUNT-1, -1, -1):
                # If that particlar spot is equal to '   ' that the player picks
                if self.board[row][column] == '   ':
                    # Display pieces in different colors on the board
                    if self.player_move() == 'X':
                        self.board[row][column] = self.player_move()
                    else:
                        self.board[row][column] = self.player_move()

                self.last_move = [row, column]
                self.moves += 1
                return True
            
            return False