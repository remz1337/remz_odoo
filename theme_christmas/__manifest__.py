# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Christmas Theme",
    "version" : "1.0.0",
    "author" : "Rémi Bédard-Couture",
    "category" : "Extra Tools",
	"summary": "Happy holidays!",
    'description': "For Odoo Enterprise Version 10.0, this module changes the colors of the interface and adds falling snow.",
    'maintainer': "Rémi Bédard-Couture",
    'website': 'https://github.com/remz1337',
    'images': [],
    "depends" : ["base"],
    "init_xml" : [],
    "demo_xml" : [],
        "data" : [
        'views/color_change.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}
