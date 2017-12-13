var api = {}

api.ajax = function (url, method, form, callback) {
    var request = {
        url: url,
        type: method,
        data: form,
        success: function (response) {
            var r = JSON.parse(response)
            callback(r)
        },
        error: function (err) {
            log('网络错误', error)
            var r = {
                'success': false,
                message: '网络错误'
            }
            callback(r)
        }
    }
    $.ajax(request)
}

api.get = function (url, response) {
    api.ajax(url, 'get', {}, response)
}

api.post = function (url, form, response) {
    api.ajax(url, 'post', form, response)
}

// 以上是标准的 ajax 模板
// 以下是添加的请求

api.insert = function (form, response) {
    var url = '/api'
    api.post(url, form, response)
}