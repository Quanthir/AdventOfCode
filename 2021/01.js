const fs = require('fs')

const depths = fs.readFileSync('01.txt', 'utf8').toString().split("\n").map((v) => parseInt(v))

function p1Solution1(d) {
	return d.filter((v, i, a) => a[i+1] > v).length
}

function p1Solution2(d) {
	const sum = (a, b) => a + b
	return d.filter((_, i, a) => 
		a.slice(i + 1, i + 4).reduce(sum, 0) >
		a.slice(i, i + 3).reduce(sum, 0)
	).length
}

console.log(`AoC [Day 01][Part 1] Solution 1: ${p1Solution1(depths)}`)
console.log(`AoC [Day 01][Part 2] Solution 1: ${p1Solution2(depths)}`)
