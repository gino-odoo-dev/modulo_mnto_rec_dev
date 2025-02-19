from odoo import models, fields  

class Secuencias(models.Model):
    _name = 'rec.secuencia'
    _description = 'Secuencias'
    _rec_name = 'nombre'

    codigo = fields.Char(string="Codigo", required=True)
    nombre = fields.Char(string="Nombre", required=True)