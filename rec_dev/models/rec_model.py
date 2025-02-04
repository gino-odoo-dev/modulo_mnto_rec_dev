from odoo import models, fields

class RecModel(models.Model):
    _name = 'rec.model'
    _description = 'Ficha Tecnica'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    product_id = fields.Many2one('product.template', string='Product')
    temporada_id = fields.Many2one('cl.product.temporada', string='Temporada')
