from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def api():
    form = request.form
    name = form.get('name')
    greet = form.get('greet')
    r = {}
    if name is not '' and greet is not '':
        d = dict(name=name, greet=greet)
        r['data'] = d
        r['success'] = True
    else:
        r['msg'] = '不能为空'
    return json.dumps(r, ensure_ascii=False)


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)
