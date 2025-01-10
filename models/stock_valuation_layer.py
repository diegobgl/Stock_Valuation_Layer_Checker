from odoo import models

class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    def action_create_accounting_entries(self):
        """
        Crear asientos contables para las capas seleccionadas.
        Este método llama a `_validate_accounting_entries` para generar las entradas.
        """
        self._validate_accounting_entries()  # Este es el método correcto
