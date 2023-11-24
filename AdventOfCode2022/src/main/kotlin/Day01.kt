import java.io.File
import java.util.*

fun main() {
    fun parseInput(input: String): List<List<Int>> {
        val data = input.split("\r\n\r\n").map { elf ->
            elf.lines().map { it.toInt() }
        }
        return data
    }

    // O(size * log size)
    fun List<List<Int>>.slowesttopNElves(n:Int): Int {
        return map {it.sum() }
        .sortedDescending()
        .take(n)
        .sum()
    }

    //O(size * log n)
    fun List<List<Int>>.slowtopNElves(n:Int): Int {
        val best = PriorityQueue<Int>()
        for (calories in map {it.sum()}) {
            best.add(calories)
            if (best.size > n) {
                best.poll()
            }
        }
        return best.sum()
    }

    //O(size)
    fun List<List<Int>>.topNElves(n:Int): Int {
        fun findTopN(n: Int, element: List<Int>): List<Int> {
            if (element.size == n) return element
            val x = element.random()
            val small = element.filter{ it < x }
            val equal = element.filter{ it == x }
            val big = element.filter{ it > x }
            if (big.size >= n) return findTopN(n, big)
            if (equal.size + big.size >= n) return (equal + big).takeLast(n)
            return findTopN(n-equal.size - big.size, small) + equal + big

        }
        return findTopN(n, this.map {it.sum()}).sum()
    }

    fun part1(input: String): Int {
        val data = parseInput(input)
        return data.topNElves(1)
    }

    fun part2(input:String): Int{
        val data = parseInput(input)
        return data.topNElves(3)
    }

//    fun part2Optimised()

    val testInput = File("src/Day01_test.txt").readText()
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = File("src/Day01.txt").readText()
    val part1Solution = part1(input)
    println("The solution to Part 1 is $part1Solution")
    println("The solution to Part 1 is "+part2(input))
}