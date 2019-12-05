package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("../input.txt")
	input := string(bytes)
	inputSlice := strings.Split(input, "-")
	rangeLow, _ := strconv.Atoi(inputSlice[0])
	rangeHigh, _ := strconv.Atoi(inputSlice[1])

	c := part1(rangeLow, rangeHigh)
	fmt.Println("Part 1:", c)
	c = part2(rangeLow, rangeHigh)
	fmt.Println("Part 2:", c)
}

func part1(low, high int) int {
	counter := 0
	for i := low; i < high; i++ {
		pwCandidate := strconv.Itoa(i)
		if validatePart1(pwCandidate) {
			counter++
		}
	}
	return (counter)
}

func validatePart1(pwCandidate string) bool {
	prev := rune(pwCandidate[0])
	seenAdjacent := false
	for _, cur := range pwCandidate[1:] {
		if cur < prev {
			return false
		}
		if prev == cur {
			seenAdjacent = true
		}

		prev = cur
	}
	return seenAdjacent
}

func part2(bottom, top int) int {
	counter := 0
	for i := bottom; i < top; i++ {
		pwCandidate := strconv.Itoa(i)
		if validatePart2(pwCandidate) && validatePart1(pwCandidate) {
			counter++
		}
	}
	return (counter)
}

// trick: we don't need to worry whether we count adjacent digits since
// the sequence is validated to be monotonically increasing in validatePart1()
// which guarantees ordering.
// So it's enough to find one digit which occurs exactly twice.
func validatePart2(pwCandidate string) bool {
	digitCount := map[rune]int{}
	for _, r := range pwCandidate {
		digitCount[r]++
	}
	for _, v := range digitCount {
		if v == 2 {
			return true
		}
	}
	return false
}
