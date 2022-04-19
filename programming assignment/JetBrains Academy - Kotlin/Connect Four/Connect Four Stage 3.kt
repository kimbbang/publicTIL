package connectfour

import kotlin.system.exitProcess

const val EMPTY = " "

fun main() {

    println("Connect Four\nFirst player's name:")
    val firstPlayer = readln()
    println("Second player's name:")
    val secondPlayer = readln()

    val (column, row) = getBoardSize()   // 6 x 7
    val board = MutableList(row) { MutableList(column) { EMPTY } }
    println("$firstPlayer VS $secondPlayer\n$row X $column board")

    drawGameBoard(board)
    startGame(firstPlayer, secondPlayer, board)
}


fun startGame(firstPlayer: String, secondPlayer: String, board: MutableList<MutableList<String>>) {

    var index = 0
    while (true) {

        var userName = if (index % 2 == 0) firstPlayer else secondPlayer
        var disk = if (index % 2 == 0) "o" else "*"

        var userColumn = getSelectedColumn(userName, board)

        for (rowIndex in (0 until board.size).reversed()) {
            if (board[rowIndex][userColumn] == EMPTY) {
                board[rowIndex][userColumn] = disk
                break
            } else {
                if (board[0][userColumn] != EMPTY) {
                    println("Column ${userColumn + 1} is full")
                    userColumn = getSelectedColumn(userName, board)
                }
            }
        }
        drawGameBoard(board)
        index += 1
    }
}


fun getSelectedColumn(turn: String, board: MutableList<MutableList<String>>): Int {

    while (true) {
        println("$turn's turn:")

        val userInput = readln()
        if (userInput == "end") {
            println("Game over!")
            exitProcess(0)
        }

        var userColumn = 0
        try {
            userColumn = userInput.toInt()
        } catch (e: NumberFormatException) {
            println("Incorrect column number")
            continue
        }

        if (userColumn < 1 || userColumn > board[0].size) {
            println("The column number is out of range (1 - ${board[0].size})")
            continue
        }

        return userColumn - 1
    }
}


fun drawGameBoard(board: MutableList<MutableList<String>>) {

    for (i in 1..board[0].size) print(" $i")   // first line
    println()

    for (row in board) {
        for (col in row) {
            print("║${col}")
        }
        println("║")
    }

    print("╚")      // last line
    for (i in 1 until board[0].size) print("═╩")
    println("═╝")
}

fun getBoardSize(): List<Int> {

    val fullyValid = Regex("\\s*\\d+\\s*[x|X]\\s*\\d+\\s*")
    val validRow = Regex("\\s*(5|6|7|8|9)\\s*[x|X]\\s*\\d*\\s*")
    val validColumn = Regex("\\s*\\d*\\s*[x|X]\\s*(5|6|7|8|9)\\s*")

    while (true) {
        println("Set the board dimensions (Rows x Columns)\nPress Enter for default (6 x 7)")
        val table = readln()

        if (table == "") {
            return listOf(7, 6)
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
            return listOf(column, row)
        }
    }
}