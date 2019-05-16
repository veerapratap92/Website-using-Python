from flask import Flask, render_template, redirect, request, url_for
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'veer@2013'

@app.route('/')
def home():
    return 'Hi'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/blog')
def blog():
    posts = [{'title':'Technology in 2019', 'author': 'pratap'},
              {'title':'Working as data scientist', 'author':'Veerapratap'}]
    return render_template('blog.html', author="Veerapratap", sunny=False,posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is the blog number' + blog_id

@app.route('/signup', methods = ['GET','POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()