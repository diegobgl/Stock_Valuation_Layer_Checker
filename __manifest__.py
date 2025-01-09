{
    'name': 'Stock Valuation Layer Checker',
    'version': '1.0',
    'summary': 'Verifica Stock Valuation Layers sin asientos contables',
    'description': """
        Este módulo permite identificar registros de Stock Valuation Layer 
        que no tienen un asiento contable asociado.
    """,
    'author': 'diego Gajardo',
    'depends': ['stock_account'],
    'data': [
        'wizard/check_valuation_layer_wizard_views.xml',
        'views/stock_valuation_layer_menu.xml',
        'views/stock_valuation_layer_action_views.xml',
    ],
    'installable': True,
    'application': False,
}
