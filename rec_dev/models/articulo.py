from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Articulo(models.Model):
    _name = 'articulo.model'
    _description = 'Articulo'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)

    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if not record.nombre or record.nombre.strip() == "":
                raise ValidationError("El nombre no puede estar vacio.")

            if len(record.nombre) != 18:
                raise ValidationError("El nombre debe tener exactamente 18 caracteres.")
