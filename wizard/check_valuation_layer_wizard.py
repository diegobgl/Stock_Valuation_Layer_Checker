from odoo import models, fields, api

class CheckValuationLayerWizard(models.TransientModel):
    _name = 'check.valuation.layer.wizard'
    _description = 'Buscar Stock Valuation Layers Sin Asientos Contables'

    start_date = fields.Date(string='Fecha Inicio', required=True)
    end_date = fields.Date(string='Fecha Fin', required=True)

    def search_valuation_layers_without_accounting(self):
        """Buscar Stock Valuation Layers sin asientos contables y con ubicaciones de tipo producción."""
        domain = [
            ('account_move_id', '=', False),  # Sin asiento contable
            ('create_date', '>=', self.start_date),  # Fecha inicio
            ('create_date', '<=', self.end_date),    # Fecha fin
            '|',  # Condición OR para considerar ambas ubicaciones (origen/destino)
            ('stock_move_id.location_id.usage', '=', 'production'),  # Ubicación origen de tipo producción
            ('stock_move_id.location_dest_id.usage', '=', 'production')  # Ubicación destino de tipo producción
        ]

        valuation_layers = self.env['stock.valuation.layer'].search(domain)

        # Retornar una acción para mostrar los resultados
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock Valuation Layers Sin Asientos',
            'res_model': 'stock.valuation.layer',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', valuation_layers.ids)],
            'context': {'create': False},  # Evitar creación de nuevos registros desde esta vista
        }
