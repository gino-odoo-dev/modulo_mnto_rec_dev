from odoo import models, fields

class Secuencia(models.Model):
    _name = 'secuencia_model'
    _description = 'Secuencia'
    _rec_name = 'codigo'

    codigo = fields.Char(string="Codigo", required=True)