package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(removeVowels("leetcodeisacommunityforcoders"))
}

func removeVowels(s string) string {
	t := []bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'z': false}

	var sb strings.Builder
	for _, r := range s {
		if !t[r] {
			sb.WriteRune(r)
		}
	}

	return sb.String()
}
