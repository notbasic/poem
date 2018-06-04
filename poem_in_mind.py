from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'hello now'

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='welcome to poetry extreme')




if __name__ == '__main__':
    app.run(debug=True)

