package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInstructions(input string) []int {
	strs := strings.Split(strings.TrimSpace(input), ",")
	instructions := make([]int, len(strs))
	for i, s := range strs {
		instruction, _ := strconv.Atoi(s)
		instructions[i] = instruction
	}
	return instructions
}

func simulate(instructions []int) {
	ip := 0
	for {
		opCode := instructions[ip]

		if opCode == 99 {
			break
		}
		if opCode == 1 {
			instructions[instructions[ip+3]] = instructions[instructions[ip+1]] + instructions[instructions[ip+2]]
		}
		if opCode == 2 {
			instructions[instructions[ip+3]] = instructions[instructions[ip+1]] * instructions[instructions[ip+2]]
		}

		ip += 4
	}
}

func part1(input string) string {
	instructions := parseInstructions(input)

	instructions[1] = 12
	instructions[2] = 2

	simulate(instructions)

	return strconv.Itoa(instructions[0])
}

func part2(input string) string {
	originalInstructions := parseInstructions(input)

	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			instructions := make([]int, len(originalInstructions))
			copy(instructions, originalInstructions)

			instructions[1] = noun
			instructions[2] = verb

			simulate(instructions)

			if instructions[0] == 19690720 {
				return strconv.Itoa(100*noun + verb)
			}
		}
	}

	return "oops, this shouldn't have happened"
}

func main() {
	bytes, _ := ioutil.ReadFile("../input.txt")

	fmt.Println("Part 1: " + part1(string(bytes)))
	fmt.Println("Part 2: " + part2(string(bytes)))
}
