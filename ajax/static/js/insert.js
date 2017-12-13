// log
var log = console.log.bind(console)

// 模板字符串
var Template = function (data) {
    var name = data.name
    var greet = data.greet
    var t = `
        <li>
            ${ greet }, ${ name }
            <button class="button">删除</button>
        </li>
    `
    return t
}

var Insert = function () {
    $('#id-button').on('click', function () {
        /*
        // 如果要发送数组，需要先转成 JSON字符串
        var l = [1, 2, 3]
        l = JSON.stringify(l)

        var name = $('#id-input-name').val()
        var greet = $('#id-input-greet').val()
        var form = {
            name: name,
            greet: greet,
            list: l,
        }
        */

        // 两个 form 是一样的

        // 如果要提交表单，选中表单以后 serialize()
        var form = $('#id-form').serialize()

        var response = function (r) {
            if (r.success) {
                var data = r.data
                $('#id-ul').prepend(Template(data))
            } else {
                var msg = r.msg
                $('#id-ul').prepend(`<li>${ msg }</li>`)
            }
        }
        api.insert(form, response)
    })
}

// 事件委托
// 新增的删除按钮不能响应事件，因为是后面动态插入到页面
// 在初始绑定的时候不存在，解决方法是把事件绑定在父节点上
// 这里是绑定在 body 上
var Delete = function () {
    $('body').on('click', '.button', function () {
        // 拿到点击按钮的 <li> 并删除
        $(this).parent('li').remove()
    })
}

var __main = function () {
    Insert()
    Delete()
}

$(document).ready(function () {
    __main();
});