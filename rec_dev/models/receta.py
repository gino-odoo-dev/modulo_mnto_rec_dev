from odoo import models, fields, api

class Temporada(models.Model):
    _name = 'temporada.model'
    _description = 'Temporada' 

class Componente(models.Model):
    _name = 'componente.model'
    _description = 'Componente' 

class Descripcion(models.Model):
    _name = 'descripcion.model'
    _description = 'Descripcion' 

class Secuencia(models.Model):
    _name = 'secuencia.model'
    _description = 'Secuencia'

class Unimedida(models.Model):
    _name = 'unimedida.model'
    _description = 'Unidad de Medida'    

class Depto(models.Model):
    _name = 'depto.model'
    _description = 'Departamento'

class Articulo(models.Model):
    _name = 'articulo.model'
    _description = 'Articulo'
    _rec_name = 'nombre' 

    nombre = fields.Char(string="Nombre", required=True)

class Compmanu(models.Model):
    _name = 'compmanu.model'
    _description = 'Compra o Manufacturado'

class Factperdida(models.Model):
    _name = 'factperdida.model'
    _description = 'Factor de Perdida'

class Cantidad(models.Model):
    _name = 'cantidad.model'
    _description = 'Cantidad'

class Cunitario(models.Model):
    _name = 'cunitario.model'
    _description = 'Costo Unitario'

class Campliado(models.Model):
    _name = 'campliado.model'
    _description = 'Costo Ampliado'

class Temporadas(models.Model):
    _name = 'cl.product.temporada'
    _description = 'Temporadas'   

class Receta(models.Model):
    _name = 'receta'
    _description = 'Receta'

    temporadas_id = fields.Many2one('cl.product.temporada', string='Temporadas', readonly=False)
    temporada_id = fields.Many2one('temporada.model', string='Temporada', readonly=False)
    componente_id = fields.Many2one('componente.model', string='Componente', readonly=True)
    descripcion_id = fields.Many2one('descripcion.model', string='Descripcion', readonly=True)
    secuencia_id = fields.Many2one('secuencia.model', string='Secuencia', readonly=True)
    uni_medida_id = fields.Many2one('unimedida.model', string='Unidad de Medida', readonly=True)
    depto_id = fields.Many2one('depto.model', string='Departamento', readonly=True)
    articulo_id = fields.Many2one('articulo.model', string='Articulo', readonly=False)
    comp_manu_id = fields.Many2one('compmanu.model', string='Compra o Manufacturado', readonly=True)

    fact_perdida_id = fields.Float(string='Factor de Pérdida (%)', readonly=False)
    cantidad_id = fields.Integer(string='Cantidad', readonly=False)
    c_unitario_id = fields.Float(string='Costo Unitario', readonly=False)
    c_ampliado_id = fields.Float(string='Costo Ampliado', compute='calcular_costo_ampliado', store=True, readonly=True)

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('next', 'Siguiente')
    ], default='draft', string="Estado")

    def next_button(self):
        self.ensure_one()
        self.state = 'next'
        self._cr.commit()

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'receta',
            'view_mode': 'tree,form',  
            'target': 'current',
            'context': {
                'default_articulo_id': self.articulo_id.id, 
                'search_default_articulo_id': self.articulo_id.id, 
            },
            'domain': [('articulo_id', '=', self.articulo_id.id)], 
        }

    @api.depends('cantidad_id', 'fact_perdida_id', 'c_unitario_id')
    def calcular_costo_ampliado(self):
        for record in self:
            if record.cantidad_id and record.fact_perdida_id and record.c_unitario_id:
                cantidad_perdida = (record.cantidad_id * record.fact_perdida_id) / 100
                record.c_ampliado_id = cantidad_perdida * record.c_unitario_id
            else:
                record.c_ampliado_id = 0

