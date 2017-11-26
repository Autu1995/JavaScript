// 打印对象
var items = function (d) {
    var description = ""
    for (var i in d) {
        var property = d[i]
        description += i + " = " + property + "\n"
    }
    return description
}
