package connectfour

import kotlin.system.exitProcess

const val EMPTY = " "
const val FIRST_PLAYER_DISK = "o"
const val SECOND_PLAYER_DISK = "*"
const val TOP_LINE = 0
const val DEFAULT_TABLE = ""
const val SINGLE_PLAY = 1
const val STATUS_WIN = 1
const val STATUS_DRAW = 0
const val STATUS_PLAYING = -1


fun main() {
    println("Connect Four")
    println("First player's name:")
    val firstPlayer = readln()
    println("Second player's name:")
    val secondPlayer = readln()

    val (column, row) = getBoardSize()   // 6 x 7
    val totalGameNumber = getNumberOfGames()

    println("$firstPlayer VS $secondPlayer")
    println("$row X $column board")

    if (totalGameNumber != SINGLE_PLAY) println("Total $totalGameNumber games")
    else println("Single game")

    var score = mutableListOf<Int>(0, 0)
    var index = 0
    for (gameNumber in SINGLE_PLAY..totalGameNumber) {

        if (totalGameNumber != SINGLE_PLAY) println("Game #$gameNumber")

        val board = MutableList(row) { MutableList(column) { EMPTY } }
        drawGameBoard(board)

        while (true) {

            var userName = if (index % 2 == 0) firstPlayer else secondPlayer
            var disk = if (index % 2 == 0) FIRST_PLAYER_DISK else SECOND_PLAYER_DISK

            var selectedColumn = getSelectedColumn(userName, board)

            for (rowIndex in (0 until board.size).reversed()) {
                if (board[rowIndex][selectedColumn] == EMPTY) {
                    board[rowIndex][selectedColumn] = disk
                    break
                }
            }
            drawGameBoard(board)

            val gameStatus = checkStatus(userName, board)
            if (totalGameNumber != SINGLE_PLAY && gameStatus != STATUS_PLAYING) {
                if (gameStatus == STATUS_WIN) {
                    score[index % 2] += 2
                } else {  // (gameStatus == STATUS_DRAW)
                    score[0] += 1
                    score[1] += 1
                }
                println("Score")
                println("$firstPlayer: ${score[0]} $secondPlayer: ${score[1]}")
            }
            index += 1
            if (gameStatus != STATUS_PLAYING) break
        }
    }
    println("Game over!")
}

fun checkStatus(userName: String, board: MutableList<MutableList<String>>): Int {

    val horizontal = listOf(listOf(0, 3), listOf(0, 2), listOf(0, 1))
    val vertical = listOf(listOf(3, 0), listOf(2, 0), listOf(1, 0))
    val leftDiagonal = listOf(listOf(3, 3), listOf(2, 2), listOf(1, 1))
    val rightDiagonal = listOf(listOf(1, -1), listOf(2, -2), listOf(3, -3))
    val lineList = listOf(horizontal, vertical, leftDiagonal, rightDiagonal)

    var gameOver = true

    for (line in lineList) {
        for (rowIndex in 0 until board.size) {
            for (colIndex in 0 until board[TOP_LINE].size) {

                var somebodyWon = true
                for (coordinates in line) {
                    val (row, column) = coordinates
                    if (board[rowIndex][colIndex] == EMPTY) {
                        somebodyWon = false
                        gameOver = false
                        break
                    }

                    if (rowIndex + row >= board.size || colIndex + column >= board[TOP_LINE].size
                        || rowIndex + row < 0 || colIndex + column < 0
                    ) {
                        somebodyWon = false
                        break
                    }

                    if (board[rowIndex + row][colIndex + column] != board[rowIndex][colIndex]) {
                        somebodyWon = false
                        break
                    }
                }

                if (somebodyWon) {
                    println("Player $userName won")
                    return STATUS_WIN
                }
            }
        }
    }
    if (gameOver) {
        println("It is a draw")
        return STATUS_DRAW
    }
    return STATUS_PLAYING
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

        if (userColumn < 1 || userColumn > board[TOP_LINE].size) {
            println("The column number is out of range (1 - ${board[TOP_LINE].size})")
            continue
        }

        if (board[TOP_LINE][userColumn - 1] != EMPTY) {
            println("Column ${userColumn + 1} is full")
            continue
        }
        return userColumn - 1
    }
}

fun drawGameBoard(board: MutableList<MutableList<String>>) {
    // first line
    for (i in 1..board[TOP_LINE].size) print(" $i")
    println()

    // middle lines
    for (row in board) {
        for (col in row) {
            print("║${col}")
        }
        println("║")
    }

    // last line
    print("╚")
    for (i in 1 until board[TOP_LINE].size) print("═╩")
    println("═╝")
}


fun getNumberOfGames(): Int {
    while (true) {
        println("Do you want to play single or multiple games?")
        println("For a single game, input 1 or press Enter")
        println("Input a number of games:")
        val tmp = readln()
        if (tmp == "") return 1
        if (tmp == "0") {
            println("Invalid input")
            continue
        }
        try {
            return tmp.toInt()
        } catch (e: NumberFormatException) {
            println("Invalid input")
        }
    }
}

fun getBoardSize(): List<Int> {

    val fullyValid = Regex("\\s*\\d+\\s*[x|X]\\s*\\d+\\s*")
    val validRow = Regex("\\s*(5|6|7|8|9)\\s*[x|X]\\s*\\d*\\s*")
    val validColumn = Regex("\\s*\\d*\\s*[x|X]\\s*(5|6|7|8|9)\\s*")

    while (true) {
        println("Set the board dimensions (Rows x Columns)")
        println("Press Enter for default (6 x 7)")

        val table = readln()

        if (table == DEFAULT_TABLE) {
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