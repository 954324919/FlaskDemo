#-*- coding=utf-8 -*-
from flask import Flask,render_template,abort,request,flash,redirect
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_script import Manager

app = Flask(__name__)
Bootstrap(app)
nav=Nav()
manager=Manager(app)


nav.register_element('top',Navbar(u'Flask入门',View(u'主页','index'),
                                  View(u'关于','about')))

nav.init_app(app)
app.config.from_pyfile("config")
@app.route('/',methods=['GET','POST'])
def main():

    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        #print 'post'+username
        #print 'post'+password
        if username=='chendaqian' and password=='chendaqian':
            return redirect(url_for('index'))
    elif request.method=='GET':
        #username=request.args['username'] #这种表示get请求获取参数
        print '111'
    return render_template('login.html',method=request.method)
    '''
    from form import LoginForm
    form=LoginForm()
    return render_template('login.html',method=request.method,form=form)
    '''

@app.route('/index/')
def index():
    return render_template('index.html')
@app.route('/about/')
def about():
    return render_template('resources/about.html')
@app.route('/case/')
def case():
    return render_template('resources/case.html')
@app.errorhandler(500)
@app.errorhandler(404)
def error(e):
    return render_template('utils/error.html')

@manager.command  #装饰器
def dev():
    from livereload import  Server
    live_server=Server(app.wsgi_app)
    live_server.watch('**/*.*')
    live_server.serve(open_url=True)
if __name__ == "__main__":
    #app.run(debug=True)
    manager.run(dev())