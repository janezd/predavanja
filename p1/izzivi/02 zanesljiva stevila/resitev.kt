fun main() {
    val pojavitve = IntArray(100000)
    pojavitve[1] = 1
    pojavitve[2] = 1
    for (i in 2 until 100000) {
        if (pojavitve[i] == 1) {
            val up = if (i < 50000) 2 * i else 100000
            for(f in i until up) {
                pojavitve[f] += pojavitve[f - i]
            }
        }
        else {
            pojavitve[i] = 0
        }
    }
    println(pojavitve.sum())
}