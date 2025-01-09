from odoo import models

class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    def action_create_accounting_entries(self):
        """Reutiliza la acción nativa para crear los asientos contables."""
        for layer in self:
            if not layer.account_move_id:
                # Reutilizamos el método nativo para crear el asiento contable
                layer._create_accounting_entries()
