from odoo import models, fields 

class Componente(models.Model):
    _name = 'componente.model'
    _description = 'Componente'
    _rec_name = 'descripcion'

    codigo = fields.Char(string="Codigo", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    um = fields.Char(string="Unidad de Medida")