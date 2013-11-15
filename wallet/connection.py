import config
from bitcoinrpc.connection import BitcoinConnection

def get_bitcoin_connection():
    return BitcoinConnection(
        config.rpcuser,
        config.rpcpassword,
        config.host,
        config.port
    )

def get_source_connection():
    return BitcoinConnection(
        config.rpcuser,
        config.rpcpassword,
        config.source_host,
        config.source_port
    )


def get_mek_connection(host):
    return BitcoinConnection(
        config.rpcuser,
        config.rpcpassword,
        host,
        config.source_port
    )
