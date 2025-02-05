from odoo import models, fields, api

class RecModel(models.Model):
    _name = 'rec.model'
    _description = 'Ficha Tecnica'

    name = fields.Char(string='Name', required=False)
    description = fields.Text(string='Description')
    product_id = fields.Many2one('product.template', string='Product')
    temporada_id = fields.Many2one('cl.product.temporada', string='Temporada')
    articulo = fields.Char(string='Articulo', store=False)

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('next', 'Siguiente')
    ], default='draft', string="Estado")

    def next_button(self):
        for record in self:
            record.state = 'next'
        return {
            'type': 'ir.actions.act_window',
            'name': 'Mnto Ficha Tecnica',
            'res_model': 'rec.model',
            'view_mode': 'tree',
            'view_id': self.env.ref('rec_dev.view_rec_model_tree').id,
            'target': 'current',
        }
    