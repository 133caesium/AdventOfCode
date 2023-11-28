import java.io.File

fun String.parseInput(): List<String> {
    return this.split("\r\n")
}

fun part1(input: List<String>): Int {
    return 0
}

fun part2(input: List<String>): Int {
    return 0
}

fun main() {
    val input = File("src/Day03.txt").readText().parseInput()
    val testInput = File("src/Day03_test.txt").readText().parseInput()

    check(part1(testInput) == 0)
    println("Part 1 Solution: "+part1(input))
    check(part2(testInput) == 0)
    println("Part 2 Solution: "+part2(input))
}
