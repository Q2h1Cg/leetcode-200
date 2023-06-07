package main

import (
	"fmt"
	"math"
)

type ArrayReader []int

func (a ArrayReader) get(index int) int {
	if index >= len(a) {
		return math.MaxInt32
	}

	return a[index]
}

func main() {
	a := ArrayReader([]int{-1, 0, 3, 5, 9, 12})
	i := search(a, 2)
	fmt.Println(i)
}

func search(reader ArrayReader, target int) int {
	if reader.get(0) == target {
		return 0
	}

	l, r := 0, 1
	for reader.get(r) < target {
		l = r
		r *= 2
	}

	for l <= r {
		m := l + (r-l)/2
		n := reader.get(m)
		if n < target {
			l = m + 1
		} else if n > target {
			r = m - 1
		} else {
			return m
		}
	}

	return -1
}
