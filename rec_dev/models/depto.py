from odoo import models, fields

class Depto(models.Model):
    _name = 'depto.model'
    _description = 'Departamento'
    _rec_name = 'descripcion'

    nombre = fields.Char(string="Nombre", required=True)
    codigo = fields.Char(string="Codigo", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    