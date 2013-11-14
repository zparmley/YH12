import StringIO

from flask import Flask, make_response, render_template
import qrcode

app = Flask(__name__)

@app.route('/')
def hi():
    return render_template('base.html')

@app.route('/testqr')
def testqr():
    try:
        img = qrcode.make('blah blah blah')
        out = StringIO.StringIO()
        img.save(out)

        resp = make_response(out.getvalue())
        resp.content_type = 'image/png'
    except Exception as e:
        return '%r' % e
    return resp

if __name__ == "__main__":
    app.run()
