import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack

nets = dict(
    bitcoin=math.Object(
        P2P_PREFIX='f9beb4d9'.decode('hex'),
        P2P_PORT=8333,
        ADDRESS_VERSION=0,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='BTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='https://blockchain.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='https://blockchain.info/address/',
        TX_EXPLORER_URL_PREFIX='https://blockchain.info/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
    bitcoin_testnet=math.Object(
        P2P_PREFIX='0b110907'.decode('hex'),
        P2P_PORT=18333,
        ADDRESS_VERSION=111,
        RPC_PORT=18332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='tBTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    litecoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=9333,
        ADDRESS_VERSION=48,
        RPC_PORT=9332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'litecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='LTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Litecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Litecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.litecoin'), 'litecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    litecoin_testnet=math.Object(
        P2P_PREFIX='fcc1b7dc'.decode('hex'),
        P2P_PORT=19333,
        ADDRESS_VERSION=111,
        RPC_PORT=19332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'litecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='tLTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Litecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Litecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.litecoin'), 'litecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/address/',
        TX_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    terracoin=math.Object(
        P2P_PREFIX='42babe56'.decode('hex'),
        P2P_PORT=13333,
        ADDRESS_VERSION=0,
        RPC_PORT=13332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='TRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),  
    terracoin_testnet=math.Object(
        P2P_PREFIX='41babe56'.decode('hex'),
        P2P_PORT=23333,
        ADDRESS_VERSION=111,
        RPC_PORT=23332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='tTRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    stablecoin=math.Object(
        P2P_PREFIX='fcc3b4da'.decode('hex'),
        P2P_PORT=17500,
        ADDRESS_VERSION=125,
        RPC_PORT=17501,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'StableCoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 25*100000000 >> (height + 1)//1080000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=45,
        SYMBOL='SBC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'StableCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/StableCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.StableCoin'), 'StableCoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://coinminer.net:2750/chain/StableCoin/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://coinminer.net:2750/chain/StableCoin/address/',
        TX_EXPLORER_URL_PREFIX='http://coinminer.net:2750/chain/StableCoin/transaction/',
	SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    zetacoin=math.Object(
        P2P_PREFIX='fab503df'.decode('hex'), #chainparams.cpp pchMessageStart
        P2P_PORT=17333,
        ADDRESS_VERSION=80, #PUBKEY_ADDRESS
        RPC_PORT=9332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'zetacoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1000*100000000 >> (height + 1)//80640,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=30, # s
        SYMBOL='ZET',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Zetacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Zetacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.zetacoin'), 'zetacoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/address/',
	TX_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    feathercoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=9336,
        ADDRESS_VERSION=14,
        RPC_PORT=9337,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'feathercoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 200*100000000 >> (height + 1)//3360000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='FTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://cryptocoinexplorer.com:5750/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://cryptocoinexplorer.com:5750/address/',
        TX_EXPLORER_URL_PREFIX='http://cryptocoinexplorer.com:5750/transaction/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    digitalcoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=7999,
        ADDRESS_VERSION=30,
        RPC_PORT=7998,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'digitalcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*10000000 >> (height + 1)//4730400,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=20, # s targetspacing
        SYMBOL='DGC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'digitalcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/digitalcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.digitalcoin'), 'digitalcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://dgc.cryptocoinexplorer.com/transaction/',
        SANE_TARGET_RANGE=(2**256//100000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    worldcoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=11081,
        ADDRESS_VERSION=73,
        RPC_PORT=11082,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'worldcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 32*10000000 >> (height + 1)//2650000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=15, # s targetspacing
        SYMBOL='WDC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'worldcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/worldcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.worldcoin'), 'worldcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://wdc.cryptocoinexplorer.com/transaction/',
        SANE_TARGET_RANGE=(2**256//100000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    doubloons=math.Object(
        P2P_PREFIX='fcd9b7dd'.decode('hex'),
        P2P_PORT=1336,
        ADDRESS_VERSION=24,
        RPC_PORT=1337,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'doubloons address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*10000000 >> (height + 1)//1080000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=30, # s targetspacing
        SYMBOL='DBL',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'doubloons') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Doubloons/') if platform.system() == 'Darwin' else os.path.expanduser('~/.doubloons'), 'doubloons.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.doubloons.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.doubloons.net/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.doubloons.net/transaction/',
        SANE_TARGET_RANGE=(2**256//100000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
    bytecoin=math.Object(
        P2P_PREFIX='f9beef69'.decode('hex'),
        P2P_PORT=6333,
        ADDRESS_VERSION=18,
        RPC_PORT=6332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='BTE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bytecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bytecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bytecoin'), 'bytecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://blockexplorer.bytecoin.in/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://blockexplorer.bytecoin.in/address/',
	TX_EXPLORER_URL_PREFIX='http://blockexplorer.bytecoin.in/transaction/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    asiccoin=math.Object(
        P2P_PREFIX='fab5e8db'.decode('hex'),
        P2P_PORT=13434,
        ADDRESS_VERSION=22,
        RPC_PORT=13435,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'asiccoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height * 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=45, # s
        SYMBOL='ASC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'asiccoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/asiccoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.asiccoin'), 'asiccoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/address/',
	TX_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    joulecoin=math.Object(
        P2P_PREFIX='a5c07955'.decode('hex'),
        P2P_PORT=26789,
        ADDRESS_VERSION=43,
        RPC_PORT=8844,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'joulecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 16*100000000 >> (height * 1)//1401600,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=45, # s
        SYMBOL='XJO',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'joulecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/joulecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.joulecoin'), 'joulecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://xjo-explorer.cryptohaus.com:2750/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://xjo-explorer.cryptohaus.com:2750/address/',
	TX_EXPLORER_URL_PREFIX='http://xjo-explorer.cryptohaus.com:2750/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    unobtanium=math.Object(
        P2P_PREFIX='03d5b503'.decode('hex'), #messagestart
        P2P_PORT=65534,
        ADDRESS_VERSION=130, #pubkey_address
        RPC_PORT=65535,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'unobtaniumaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.001*100000000 if height<2000  else 1*100000000 >> (height * 1)//120000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=180, # s
        SYMBOL='Un',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unobtanium') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unobtanium/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unobtanium'), 'unobtanium.conf'),
	BLOCK_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/block/',
	ADDRESS_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/address/',
	TX_EXPLORER_URL_PREFIX='http://bit.usr.sh:2750/tx/',
	SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    dogecoin=math.Object(
        P2P_PREFIX='c0c0c0c0'.decode('hex'),
        P2P_PORT=22556,
        ADDRESS_VERSION=30,
        RPC_PORT=22555,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'dogecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 10000*100000000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=60, # s
        SYMBOL='DOGE',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'DogeCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Dogecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.dogecoin'), 'dogecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://dogechain.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://dogechain.info/address/',
        TX_EXPLORER_URL_PREFIX='http://dogechain.info/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    fastcoinsha=math.Object(
        P2P_PREFIX='03020404'.decode('hex'), #messagestart
        P2P_PORT=65505,
        ADDRESS_VERSION=36, #pubkey_address
        RPC_PORT=65504,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'fastcoinshaaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 10*100000000 >> (height * 1)//40320 if height < 120960 else (10*100000000 >> (height * 1)//40320) + height,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=180, # s
        SYMBOL='FSS',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'fastcoinsha') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/fastcoinsha/') if platform.system() == 'Darwin' else os.path.expanduser('~/.fastcoinsha'), 'fastcoinsha.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://fss.daymining.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://fss.daymining.com/address/',
        TX_EXPLORER_URL_PREFIX='http://fss.daymining.com/block/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
chikun=math.Object(
        P2P_PREFIX='88b4e39c'.decode('hex'), #messagestart
        P2P_PORT=41255,
        ADDRESS_VERSION=28, #pubkey_address
        RPC_PORT=41254,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'chikunaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 100*100000000 >> (height + 1)//43800,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=60, # s
        SYMBOL='KUN',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'chikun') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/chikun/') if platform.system() == 'Darwin' else os.path.expanduser('~/.chikun'), 'chikun.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://blockchain.chikun.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://blockchain.chikun.info/address/',
        TX_EXPLORER_URL_PREFIX='http://blockchain.chikun.info/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
parallelcoinscrypt=math.Object(
        P2P_PREFIX='cd08acff'.decode('hex'), #messagestart
        P2P_PORT=11047,
        ADDRESS_VERSION=83, #pubkey_address
        RPC_PORT=11048,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'parallelcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.02*100000000 if height < 999  else 2*100000000 >> (height * 1)//250000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s
        SYMBOL='DUO SCRYPT',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'parallelcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/parallelcoin') if platform.system() == 'Darwin' else os.path.expanduser('~/.parallelcoin'), 'parallelcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/address/',
        TX_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),
parallelcoinsha=math.Object(
        P2P_PREFIX='cd08acff'.decode('hex'), #messagestart
        P2P_PORT=11047,
        ADDRESS_VERSION=83, #pubkey_address
        RPC_PORT=11048,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'parallelcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.02*100000000 if height < 999  else 2*100000000 >> (height * 1)//250000, 
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=300, # s
        SYMBOL='DUO SHA',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'parallelcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/parallelcoin') if platform.system() == 'Darwin' else os.path.expanduser('~/.parallelcoin'), 'parallelcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/address/',
        TX_EXPLORER_URL_PREFIX='http://duo.broketech.net:3000/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    vikingcoin=math.Object(
        P2P_PREFIX='55424b45'.decode('hex'), #messagestart
        P2P_PORT=11066,
        ADDRESS_VERSION=70, #pubkey_address
        RPC_PORT=11067,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Vikingaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*10000000 if height<1000 else 10*100000000 if height<2000 else 1*10000000 >> (height * 1)//100000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=90, # s
        SYMBOL='VIK',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'vikingcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/vikingcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.vikingcoin'), 'vikingcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
