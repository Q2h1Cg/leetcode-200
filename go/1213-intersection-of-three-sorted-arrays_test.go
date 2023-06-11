package main

import (
	"math"
	"reflect"
	"testing"
)

func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
	var ans []int
	i, j, k := 0, 0, 0
	for i < len(arr1) && j < len(arr2) && k < len(arr3) {
		if arr1[i] == arr2[j] && arr1[i] == arr3[k] {
			ans = append(ans, arr1[i])
			i++
			j++
			k++
			continue
		}

		min := int(math.Min(
			math.Min(float64(arr1[i]), float64(arr2[j])),
			math.Min(float64(arr1[i]), float64(arr3[k])),
		))
		switch min {
		case arr1[i]:
			i++
		case arr2[j]:
			j++
		case arr3[k]:
			k++
		}
	}

	return ans
}

func TestArraysIntersection(t *testing.T) {
	tests := []struct {
		name string
		arr1 []int
		arr2 []int
		arr3 []int
		want []int
	}{
		{
			name: "1",
			arr1: []int{1, 2, 3, 4, 5},
			arr2: []int{1, 2, 5, 7, 9},
			arr3: []int{1, 3, 4, 5, 8},
			want: []int{1, 5},
		},
		{
			name: "2",
			arr1: []int{197, 418, 523, 876, 1356},
			arr2: []int{501, 880, 1593, 1710, 1870},
			arr3: []int{521, 682, 1337, 1395, 1764},
			want: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := arraysIntersection(tt.arr1, tt.arr2, tt.arr3)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("arraysIntersection() got %v, want %v", got, tt.want)
			}
		})
	}
}
