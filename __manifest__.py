# -*- coding: utf-8 -*-
{
    'name': "Follow-up",

    'summary': """
        Add some feature to om_account_followup module """,

    'description': """
       Add auto excute to follow-up level
       Add action type to follow-up level
       Add reconciliation button to follow-up tap in partner form
    """,

    'author': "Arados Software",
    'website': "https://odoo.arados-co.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','om_account_followup','account_reconciliation_widget'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/cron.xml',
        'views/partner.xml',
        'views/follow_level.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
