package main

import (
	"math"
	"testing"
)

func calculateTime(keyboard string, word string) int {
	m := make(map[rune]int, len(keyboard))
	for i, r := range keyboard {
		m[r] = i
	}

	total := 0
	prev := 0
	for _, r := range word {
		pos := m[r]
		total += int(math.Abs(float64(pos - prev)))
		prev = pos
	}

	return total
}

func TestCalculateTime(t *testing.T) {
	tests := []struct {
		name     string
		keyboard string
		word     string
		want     int
	}{
		{
			name:     "1",
			keyboard: "abcdefghijklmnopqrstuvwxyz",
			word:     "cba",
			want:     4,
		},
		{
			name:     "2",
			keyboard: "pqrstuvwxyzabcdefghijklmno",
			word:     "leetcode",
			want:     73,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := calculateTime(tt.keyboard, tt.word)
			if got != tt.want {
				t.Errorf("calculateTime() got %d, want %d", got, tt.want)
			}
		})
	}
}
