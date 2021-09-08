#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from flask import Flask, request, escape, make_response, render_template, session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def fast_flask():
    name = request.args.get('name', 'world')
    return f'Hello,{name}'


@app.route('/login', methods=['post', 'get'])
def login():
    res = {
        'methods': request.method,
        'url': request.path,
        'name': request.args.get('name'),
        'args': request.args,
        'form': request.form
    }
    # username = request.cookies.get('name')
    # resp = make_response(render_template('name'))
    # resp.set_cookie('name', 'zhihuan')
    session['name'] = request.args.get('name')
    return res


if __name__ == '__main__':
    app.run(debug=True)
