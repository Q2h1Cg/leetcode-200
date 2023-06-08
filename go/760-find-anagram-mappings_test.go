package main

import "testing"

func anagramMappings(nums1 []int, nums2 []int) []int {
	m := make(map[int]int, len(nums1))
	for i, n := range nums2 {
		m[n] = i
	}

	p := make([]int, len(nums1))
	for i, n := range nums1 {
		p[i] = m[n]
	}

	return p
}

func equal(s1, s2 []int) bool {
	if len(s1) != len(s2) {
		return false
	}

	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			return false
		}
	}

	return true
}

func TestAnagramMappings(t *testing.T) {
	tests := []struct {
		name  string
		nums1 []int
		nums2 []int
		want  []int
	}{
		{
			"case 1",
			[]int{12, 28, 46, 32, 50},
			[]int{50, 12, 32, 46, 28},
			[]int{1, 4, 3, 2, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := anagramMappings(tt.nums1, tt.nums2)
			if !equal(got, tt.want) {
				t.Errorf("anagramMappings() got %v, want %v", got, tt.want)
			}
		})
	}
}
