import java.io.File

fun main() {
    fun part1(input: String): Int {
        val data = input.split("\r\n\r\n").map{ elf ->
            elf.lines().map{ it.toInt() }
        }
        return data.maxOf { it.sum() }
    }

    fun part2(input: List<String>): Int{
        return input.size
    }

    val testInput = File("src/Day01_test.txt").readText()
    check(part1(testInput) == 24000)

    val input = File("src/Day01.txt").readText()
    val part1Solution = part1(input)
    println("The solution to Part 1 is $part1Solution")
//    println(part2(input))
}