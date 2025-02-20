from odoo import models, fields

class CopiaFicha(models.Model):
    _name = 'copiaficha.model'
    _description = 'Copia Ficha Tecnica'

    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripcion')
