from odoo import models, fields, api

class CheckValuationLayerWizard(models.TransientModel):
    _name = 'check.valuation.layer.wizard'
    _description = 'Buscar Stock Valuation Layers Sin Asientos Contables'

    start_date = fields.Date(string='Fecha Inicio', required=True)
    end_date = fields.Date(string='Fecha Fin', required=True)

    def search_valuation_layers_without_accounting(self):
        """Buscar Stock Valuation Layers sin asientos contables agrupados por valorización."""
        domain = [
            ('account_move_id', '=', False),  # Sin asiento contable
            ('create_date', '>=', self.start_date),  # Fecha inicio
            ('create_date', '<=', self.end_date),    # Fecha fin
        ]

        valuation_layers = self.env['stock.valuation.layer'].search(domain)

        # Crear un conjunto único basado en un campo agrupador
        grouped_layers = {}
        for layer in valuation_layers:
            key = layer.id  # Reemplazar con el campo adecuado, como `valuation_id`
            if key not in grouped_layers:
                grouped_layers[key] = layer

        # Retornar una acción para mostrar los resultados agrupados
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stock Valuation Layers Sin Asientos',
            'res_model': 'stock.valuation.layer',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', list(grouped_layers.keys()))],
            'context': {'create': False},  # Evitar creación de nuevos registros desde esta vista
        }
