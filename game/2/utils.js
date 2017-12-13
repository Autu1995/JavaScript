var log = console.log.bind(console)

// 取图片的函数
var imageFromPath = function (path) {
    var img = new Image()
    img.src = path
    return img
}

// 判断球与砖块碰撞的函数
var rectIntersects = function (a, b) {
    var o = a
    if (b.y > o.y && b.y < o.y + o.image.height) {
        if (b.x > o.x && b.x < o.x + o.image.width) {
            return true
        }
    }
    return false
}
