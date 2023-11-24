import java.io.File

fun main() {
    fun parseInput(input: String): List<Int> {
        val data = input.split("\r\n\r\n").map { elf ->
            elf.lines().sumOf { it.toInt() }
        }
        return data
    }

    fun part1(input: String): Int {
        val data = parseInput(input)
        return data.maxOrNull() ?: 0
    }

    fun part2(input:String): Int{
        val data = parseInput(input)
        return data
            .sortedDescending()
            .take(3)
            .sum()
    }

    val testInput = File("src/Day01_test.txt").readText()
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = File("src/Day01.txt").readText()
    val part1Solution = part1(input)
    println("The solution to Part 1 is $part1Solution")
    println("The solution to Part 1 is "+part2(input))
}