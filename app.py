import StringIO

from flask import Flask, make_response, render_template
import qrcode

app = Flask(__name__)

# app.config['SERVER_NAME'] = 'dev2-devc.dev.yelpcorp.com:35535'

@app.route('/')
def hi():
	return render_template('base.html')

@app.route('/testqr')
def testqr():
    try:
        img = qrcode.make('http://www.yelp.com')
        out = StringIO.StringIO()
        img.save(out)

        resp = make_response(out.getvalue())
        resp.content_type = 'image/png'
    except Exception as e:
        return '%r' % e
    return resp


@app.route('/qr/vote_yea')
def vote_yea():
    out = StringIO.StringIO()
    qrcode.make('bitcoin:msheGGqfR2wYCTUxCbi2zc5jMAeyFySYfz?amount=.001').save(out)
    resp = make_response(out.getvalue())
    resp.content_type = 'image/png'
    return resp


@app.route('/qr/vote_nay')
def vote_nay():
    out = StringIO.StringIO()
    qrcode.make('bitcoin:n2ZtCWod8yYSD7fZzs9NyqyiehQZU62kbg?amount=.001&label=nono%20you%20loose').save(out)
    resp = make_response(out.getvalue())
    resp.content_type = 'image/png'
    return resp


@app.route('/qr/download_ios')
def qr_download_ios():
    out = StringIO.StringIO()
    qrcode.make('itms-apps://itunes.com/apps/blockchain').save(out)
    resp = make_response(out.getvalue())
    resp.content_type = 'image/png'
    return resp


@app.route('/qr/download_android')
def qr_download_android():
    out = StringIO.StringIO()
    qrcode.make('market://details?id=de.schildbach.wallet').save(out)
    resp = make_response(out.getvalue())
    resp.content_type = 'image/png'
    return resp


@app.route('/testvidya')
def testvidya():
    return render_template('testvidya.html')


@app.route('/grab')
def grab():
	try:
		return render_template('grab.html')
	except Exception as e:
		return '%r' % e

@app.route('/vote_to_choose')
def vote():
    return render_template('vote_to_choose.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
