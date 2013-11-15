import StringIO

from flask import Flask, make_response, render_template
import qrcode

from config.votes import votes as votes_config

app = Flask(__name__)

# app.config['SERVER_NAME'] = 'dev2-devc.dev.yelpcorp.com:35535'

@app.route('/')
def hi():
	return render_template('base.html')

#In [27]: [(x.account, x.txid, get_transaction_from(x.txid)) for x in mek.listtransactions(count=100000000000)]


@app.route('/testqr')
def testqr():
    try:
        img = qrcode.make('market://details?id=com.google.android.apps.maps')
        out = StringIO.StringIO()
        img.save(out)

        resp = make_response(out.getvalue())
        resp.content_type = 'image/png'
    except Exception as e:
        return '%r' % e
    return resp


@app.route('/qr/vote/<vote>')
def vote_qr_code(vote):
    if vote not in votes_config:
        return None
    out = StringIO.StringIO()
    qrcode.make('bitcoin:%s?amount=%s&label=%s' % (votes_config[vote]['address'], votes_config[vote]['ammount'], votes_config[vote]['label'])).save(out)
    resp = make_response(out.getvalue())
    resp.content_type = 'image/png'
    return resp


@app.route('/testvidya')
def testvidya():
    return render_template('testvidya.html')


@app.route('/grab')
def grab():
	try:
		return render_template('testvidya.html')
	except Exception as e:
		return '%r' % e

@app.route('/vote_to_choose')
def vote():
    return render_template('vote_to_choose.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
