package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func handle_err(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	file, err := os.Open("C:/Users/rob_k/Documents/advent_of_code/2022/inputs/Day_1_input.txt")
	handle_err(err)

	scanner := bufio.NewScanner(file)
	tally, third_place, second_place, highest_score := 0, 0, 0, 0
	for scanner.Scan() {
		line := scanner.Text()
		if strings.TrimSpace(line) == "" {
			if tally > highest_score {
				third_place, second_place, highest_score = second_place, highest_score, tally
				highest_score = tally
			}
			tally = 0
		} else {
			num, err := strconv.Atoi(line)
			handle_err(err)
			tally += num
		}
	}

	fmt.Println("pt1 answer is:", highest_score)
	total := third_place + second_place + highest_score
	fmt.Println("pt2 answer is:", third_place, second_place, highest_score, "for a total of:", total)

}
