import config
from bitcoinrpc.connection import BitcoinConnection

def get_bitcoin_connection():
    return BitcoinConnection(
        config.rpcuser,
        config.rpcpassword,
        config.host,
        config.port
    )
