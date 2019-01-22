# -*- coding: utf-8 -*-
{
    'name': "PortalOC",

    'summary': """
        Sistema de orden de compra para MbM Group""",

    'description': """
        Sistema de orden de compra para MbM Group
    """,

    'author': "MbM Group",
    'website': "http://www.mbmgroup.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/portal_oc_stages',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}