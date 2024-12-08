from typing import List
import re

def solve_word_puzzle(word_puzzle: List[str], pattern: str) -> int:
    pattern_count = 0
    mas_count = 0

    xmin = 0
    ymin = 0
    xmax = len(word_puzzle[0])
    ymax = len(word_puzzle)

    for y in range(ymin, ymax):
        for x in range(xmin, xmax):        
            
            forward, backward = "", ""
            forward = "".join([word_puzzle[y][x+i] for i in range(0, len(pattern)) if x+i < len(word_puzzle[0])])
            print(forward)
            backward = "".join([word_puzzle[y][x-i] for i in range(0, len(pattern)) if x-i >= 0])
            print(backward)


            upward, downward = "", ""
            upward = "".join([ word_puzzle[y-i][x] for i in range(0, len(pattern)) if y-i >= 0])
            print(upward)
            downward = "".join([word_puzzle[y+i][x] for i in range(0, len(pattern)) if y+i < len(word_puzzle)])
            print(downward)


            diagonal_up_left, diagonal_down_right = "", ""
            diagonal_up_left = "".join([word_puzzle[y-i][x-i] for i in range(0, len(pattern)) if y-i >= 0 and x-i >= 0])
            print(diagonal_up_left)
            diagonal_down_right = "".join([word_puzzle[y+i][x+i] for i in range(0, len(pattern)) if y+i < len(word_puzzle) and x+i < len(word_puzzle[0])])
            print(diagonal_down_right)

            diagonal_up_right, diagonal_down_left = "", ""
            diagonal_up_right = "".join([word_puzzle[y-i][x+i] for i in range(0, len(pattern)) if y-i >= 0 and x+i < len(word_puzzle[0])])
            print(diagonal_up_right)
            diagonal_down_left = "".join([word_puzzle[y+i][x-i] for i in range(0, len(pattern)) if y+i < len(word_puzzle) and x-i >= 0])
            print(diagonal_down_left)

            if forward == pattern:
                pattern_count += 1
            if backward == pattern:
                pattern_count += 1
            if upward == pattern:
                pattern_count += 1
            if downward == pattern:
                pattern_count += 1
            if diagonal_up_left == pattern:
                pattern_count += 1
            if diagonal_down_right == pattern:
                pattern_count += 1
            if diagonal_up_right == pattern:
                pattern_count += 1
            if diagonal_down_left == pattern:
                pattern_count += 1


            current_char = word_puzzle[y][x]
            if current_char == "A" and len(diagonal_up_left) > 1 and len(diagonal_up_right) > 1 and len(diagonal_down_left) > 1 and len(diagonal_down_right) > 1:
                d_u_l = diagonal_up_left[1]
                d_u_r = diagonal_up_right[1]
                d_d_l = diagonal_down_left[1]
                d_d_r = diagonal_down_right[1]
                
                diagonal_1 = d_u_l + current_char + d_d_r
                diagonal_2 = d_u_r + current_char + d_d_l

                if (diagonal_1 == "MAS" or diagonal_1[::-1] == "MAS") and (diagonal_2 == "MAS" or diagonal_2[::-1] == "MAS"):
                    mas_count += 1
            

            print(pattern_count)
    return pattern_count, mas_count



if __name__ == "__main__":
    with open("data/day4.txt") as f:
        word_puzzle = [line.strip() for line in f.readlines()]
        result, mas_count = solve_word_puzzle(word_puzzle, "XMAS")
        print(result)
        print(mas_count)
        
