import java.io.File

//https://adventofcode.com/2022/day/2

enum class Round(val score: Int) {
    AX(3+1),
    AY(6+2),
    AZ(0+3),
    BX(0+1),
    BY(3+2),
    BZ(6+3),
    CX(6+1),
    CY(0+2),
    CZ(3+3),
}

fun main() {
    val input = File("src/Day02.txt").readText()
    val testInput = File("src/Day02_test.txt").readText()

    fun parseInput(input: String): List<Round> {
        return input.split("\r\n").map {
            Round.valueOf(it.replace(" ",""))
        }
    }

    fun part1(input: String): Int {
        val data = parseInput(input)
        return data.map { it.score }.sum()
    }

    check(part1(testInput) == 15)
    println("Part 1 Solution: "+part1(input))

}