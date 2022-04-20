package connectfour

fun main() {

    println("Connect Four")
    println("First player's name:")
    val first = readln()
    println("Second player's name:")
    val second = readln()

    val fullyValid = Regex("\\s*\\d+\\s*[x|X]\\s*\\d+\\s*")
    val validRow = Regex("\\s*(5|6|7|8|9)\\s*[x|X]\\s*\\d*\\s*")
    val validColumn = Regex("\\s*\\d*\\s*[x|X]\\s*(5|6|7|8|9)\\s*")

    while (true) {
        println("Set the board dimensions (Rows x Columns)\nPress Enter for default (6 x 7)")
        val table = readln()

        if (table == "") {
            println("$first VS $second\n6 X 7 board")
            break
        }

        val row = validRow.matchEntire(table)?.destructured?.component1()?.toInt()
        val column = validColumn.matchEntire(table)?.destructured?.component1()?.toInt()

        if (!table.matches(fullyValid)) {
            println("Invalid input")
            continue

        } else if (row == null) {
            println("Board rows should be from 5 to 9")
            continue

        } else if (column == null) {
            println("Board columns should be from 5 to 9")
            continue

        } else {
            println("$first VS $second")
            println("$row X $column board")
            break
        }
    }
}