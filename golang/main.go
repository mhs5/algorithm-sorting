package main

import (
	"fmt"
)

func bubbleSort(unsortedArray []int) []int {
	for i := 0; i < len(unsortedArray); i++ {
		for j := 0; j < len(unsortedArray)-i-1; j++ {
			temp := 0
			if unsortedArray[j] > unsortedArray[j+1] {
				temp = unsortedArray[j]
				unsortedArray[j] = unsortedArray[j+1]
				unsortedArray[j+1] = temp
			}
		}
	}
	return unsortedArray
}

func main() {
	unsortedArray := []int{2, 6, 8, 3, 1}
	fmt.Println(bubbleSort(unsortedArray))
}
