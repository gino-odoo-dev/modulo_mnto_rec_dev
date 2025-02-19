from odoo import models, fields

class Depto(models.Model):
    _name = 'depto.model'
    _description = 'Departamento'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)