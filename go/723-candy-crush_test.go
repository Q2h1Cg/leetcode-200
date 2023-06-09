package main

import (
	"reflect"
	"testing"
)

func candyCrush(board [][]int) [][]int {
	for {
		crushed := map[[2]int]bool{}

		for i := 0; i < len(board); i++ {
			for j := 0; j < len(board[0]); j++ {
				if board[i][j] == 0 {
					continue
				}

				// 查找垂直方向相连的同种糖果
				end := i
				for ; end < len(board); end++ {
					if board[end][j] != board[i][j] {
						break
					}
				}
				if end-i > 2 {
					for x := i; x < end; x++ {
						crushed[[2]int{x, j}] = true
					}
				}

				// 查找水平方向相连的同种糖果
				end = j
				for ; end < len(board[0]); end++ {
					if board[i][end] != board[i][j] {
						break
					}
				}
				if end-j > 2 {
					for y := j; y < end; y++ {
						crushed[[2]int{i, y}] = true
					}
				}
			}
		}

		if len(crushed) == 0 {
			break
		}

		// 粉碎
		for pos := range crushed {
			board[pos[0]][pos[1]] = 0
		}

		// 掉落
		for i := len(board) - 1; i > 0; i-- {
			for {
				n := 0

				for j := 0; j < len(board[0]); j++ {
					if board[i][j] != 0 {
						continue
					}

					x := i
					for ; x > 0; x-- {
						if board[x-1][j] != 0 {
							n += 1
						}

						board[x][j] = board[x-1][j]
					}
					board[x][j] = 0
				}

				if n == 0 {
					break
				}
			}
		}
	}

	return board
}

func TestCandyCrush(t *testing.T) {
	tests := []struct {
		name  string
		board [][]int
		want  [][]int
	}{
		{
			"case 1",
			[][]int{
				{110, 5, 112, 113, 114},
				{210, 211, 5, 213, 214},
				{310, 311, 3, 313, 314},
				{410, 411, 412, 5, 414},
				{5, 1, 512, 3, 3},
				{610, 4, 1, 613, 614},
				{710, 1, 2, 713, 714},
				{810, 1, 2, 1, 1},
				{1, 1, 2, 2, 2},
				{4, 1, 4, 4, 1014},
			},
			[][]int{
				{0, 0, 0, 0, 0},
				{0, 0, 0, 0, 0},
				{0, 0, 0, 0, 0},
				{110, 0, 0, 0, 114},
				{210, 0, 0, 0, 214},
				{310, 0, 0, 113, 314},
				{410, 0, 0, 213, 414},
				{610, 211, 112, 313, 614},
				{710, 311, 412, 613, 714},
				{810, 411, 512, 713, 1014},
			},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := candyCrush(tt.board)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("candyCrush() got %v, want %v", got, tt.want)
			}
		})
	}
}
