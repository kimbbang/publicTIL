package machine

fun state(machine: MutableList<Int>) = """
The coffee machine has:
${machine[0]} ml of water
${machine[1]} ml of milk
${machine[2]} g of coffee beans
${machine[3]} disposable cups
$${machine[4]} of money


""".trimIndent()

fun cal(machine: MutableList<Int>, portion: List<Int>) {

    val names = listOf<String>("water", "milk", "beans", "cups")

    var flag = true
    for (i in 0..3) {
        if (machine[i] < portion[i]) {
            println("Sorry, not enough ${names[i]}!")
            flag = false
        }
    }

    if (flag) {
        println("I have enough resources, making you a coffee!")
        for (i in 0..3) {
            machine[i] -= portion[i]
        }
        machine[4] += portion[4]
    }
}

fun buy(machine: MutableList<Int>) {
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    when (readln()) {
        "1" -> cal(machine, listOf(250, 0, 16, 1, 4))
        "2" -> cal(machine, listOf(350, 75, 20, 1, 7))
        "3" -> cal(machine, listOf(200, 100, 12, 1, 6))
        "back" -> return
    }
}

fun fill(machine: MutableList<Int>) {
    print("Write how many ml of water do you want to add : ")
    val water = readln().toInt()
    print("Write how many ml of milk do you want to add : ")
    val milk = readln().toInt()
    print("Write how many grams of coffee beans do you want to add : ")
    val beans = readln().toInt()
    print("Write how many disposable cups of coffee do you want to add : ")
    val cups = readln().toInt()

    val portion = listOf<Int>(water, milk, beans, cups)
    for (i in 0..3) {
        machine[i] += portion[i]
    }
}

fun take(machine: MutableList<Int>) {
    println("I gave you $${machine[4]}")
    machine[4] = 0
}

fun main() {
    // water milk beans cups money
    val machine = mutableListOf<Int>(400, 540, 120, 9, 550)

    while (true) {
        print("Write action (buy, fill, take, remaining, exit): ")
        when (readln()) {
            "buy" -> buy(machine)
            "fill" -> fill(machine)
            "take" -> take(machine)
            "remaining" -> print(state(machine))
            "exit" -> return
        }
    }
}