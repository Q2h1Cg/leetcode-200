package main

import "testing"

func smallestCommonElement(mat [][]int) int {
	m := make(map[int]bool, len(mat[0]))
	for _, col := range mat[0] {
		m[col] = true
	}

	max := mat[0][len(mat[0])-1]

	for _, row := range mat[1:] {
		mNew := make(map[int]bool, len(mat[0]))
		maxNew := 0

		for _, col := range row {
			if col > max {
				break
			}

			if m[col] {
				mNew[col] = true
				maxNew = col
			}
		}

		m = mNew
		max = maxNew
	}

	if len(m) == 0 {
		return -1
	}

	min := 10000
	for k := range m {
		if k < min {
			min = k
		}
	}

	return min
}

func TestSmallestCommonElement(t *testing.T) {
	tests := []struct {
		name string
		mat  [][]int
		want int
	}{
		{
			name: "1",
			mat: [][]int{
				{1, 2, 3, 4, 5},
				{2, 4, 5, 8, 10},
				{3, 5, 7, 9, 11},
				{1, 3, 5, 7, 9},
			},
			want: 5,
		},
		{
			name: "2",
			mat: [][]int{
				{1, 2, 3},
				{2, 3, 4},
				{2, 3, 5},
			},
			want: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := smallestCommonElement(tt.mat)
			if got != tt.want {
				t.Errorf("smallestCommonElement() got %d, want %d", got, tt.want)
			}
		})
	}
}
