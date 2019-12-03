package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"strconv"
)

func part1(in io.Reader) string {
	s := bufio.NewScanner(in)

	res := 0
	for s.Scan() {
		i, _ := strconv.Atoi(s.Text())
		res += fuel(i)
	}

	return fmt.Sprint(res)
}

func part2(in io.Reader) string {
	s := bufio.NewScanner(in)

	res := 0
	for s.Scan() {
		i, _ := strconv.Atoi(s.Text())
		acc := fuel(i)
		for v := fuel(acc); v > 0; v = fuel(v) {
			acc += v
		}
		res += acc
	}

	return fmt.Sprint(res)
}

func fuel(i int) int {
	return int(math.Floor(float64(i/3))) - 2
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic("gimme input!")
	}

	reader := bufio.NewReader(file)
	fmt.Println(part1(reader))
	file.Seek(0, 0)
	fmt.Println(part2(reader))
}
