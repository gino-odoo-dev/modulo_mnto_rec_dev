from odoo import models, fields

class Compmanu(models.Model):
    _name = 'compmanu.model'
    _description = 'Compra o Manufacturado'
    _order = 'id'
    _rec_name = 'tipo'

    tipo = fields.Char(string="Nombre", required=True)