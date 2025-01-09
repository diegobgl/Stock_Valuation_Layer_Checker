{
    'name': 'Stock Valuation Layer Checker',
    'version': '1.0',
    'summary': 'Verifica Stock Valuation Layers sin asientos contables',
    'description': """
        Este módulo permite identificar registros de Stock Valuation Layer 
        que no tienen un asiento contable asociado.
    """,
    'author': 'Tu Nombre',
    'depends': ['stock_account'],
    'data': [
        'wizards/check_valuation_layer_wizard_views.xml',
        'views/stock_valuation_layer_menu.xml',
    ],
    'installable': True,
    'application': False,
}
