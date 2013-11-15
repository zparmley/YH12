import json
import re
import StringIO

from flask import Flask, make_response, render_template
import qrcode

from config.votes import votes as votes_config
from wallet.connection import get_bitcoin_connection, get_source_connection

app = Flask(__name__)


@app.route('/')
def hi():
	return render_template('base.html')

#In [27]: [(x.account, x.txid, get_transaction_from(x.txid)) for x in mek.listtransactions(count=100000000000)]

@app.route('/start')
def start():
	return render_template('start.html')


@app.route('/result')
def result():
	return render_template('result.html')


@app.route('/qr/vote/<vote>')
def vote_qr_code(vote):
    if vote not in votes_config:
        return None
    out = StringIO.StringIO()
    qrcode.make('bitcoin:%s?amount=%s&label=%s' % (votes_config[vote]['address'], votes_config[vote]['ammount'], votes_config[vote]['label'])).save(out)
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

@app.route('/grab')
def grab():
	try:
		return render_template('grab.html')
	except Exception as e:
		return '%r' % e

@app.route('/vote_to_choose')
def vote():
    return render_template('vote_to_choose.html')

@app.route('/give_away_money/<path:address>')
def give_away_money(address):
    try:
        to = re.match('bitcoin:/{0,2}([a-zA-Z0-9]{34}).*', address).group(1)
        connection = get_source_connection()
        connection.sendtoaddress(to, .002, comment="Vote with your dollars!")
    except Exception as e:
        return '%r' % e
    return 'yaay'


# meh
global seen
seen = []

@app.route('/poll_boats')
def poll_boats():
    try:
        global seen
        con = get_bitcoin_connection()
        transactions = con.listtransactions()
        relevant = [t for t in transactions if not t.txid in seen]
        for r in relevant:
            seen.append(r.txid)

        if relevant:
            resp = {'found': True, 'account': json.dumps(relevant[0].account), 'seen': seen}
        else:
            resp = {'found': False}

        resp = make_response(json.dumps(resp))
        resp.content_type = 'application/json'
        return resp
    except Exception as e:
        return '%r' % e


if __name__ == "__main__":
    app.run()
