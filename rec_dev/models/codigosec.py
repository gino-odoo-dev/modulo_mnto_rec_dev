from odoo import models, fields

class CodigoSec(models.Model):
    _name = 'codigosec.model'
    _description = 'Codigo Secuencia'
    _rec_name = 'codigo'

    codigo = fields.Char(string='CodigoSec', required=True)