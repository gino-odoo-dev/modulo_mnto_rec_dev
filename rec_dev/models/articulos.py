from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Articulos(models.Model):
    _name = 'cl.product.articulo'
    _description = 'Articulos'
    _order = 'id'
    _rec_name = 'name'

    name = fields.Char(string="Nombre", required=True)

    @api.constrains('name')
    def _check_nombre(self):
        for record in self:
            if not record.name or record.name.strip() == "":
                raise ValidationError("El nombre no puede estar vacio.")

            if len(record.name) != 18:
                raise ValidationError("El nombre debe tener exactamente 18 caracteres.")