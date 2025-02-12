from odoo import models, fields, api

class Temporada(models.Model):
    _name = 'temporada.model'
    _description = 'Temporada'

class Temporadas(models.Model):
    _name = 'cl.product.temporada'
    _description = 'Temporadas'

class Secuencia(models.Model):
    _name = 'secuencia_model'
    _description = 'Secuencia'
    _rec_name = 'codigo'

    codigo = fields.Char(string="Codigo", required=True)

class Secuencias(models.Model):
    _name = 'rec.secuencia'
    _description = 'Secuencias'
    _rec_name = 'nombre'

    codigo = fields.Char(string="Codigo", required=True)
    nombre = fields.Char(string="Nombre", required=True)

class CodigoSec(models.Model):
    _name = 'codigosec.model'
    _description = 'Codigo Secuencia'
    _rec_name = 'codigo'

    codigo = fields.Char(string='CodigoSec', required=True)

class Componente(models.Model):
    _name = 'componente.model'
    _description = 'Componente'
    _rec_name = 'codigo'

    codigo = fields.Char(string="Codigo", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    um = fields.Char(string="Unidad de Medida")
    
class Descripcion(models.Model):
    _name = 'descripcion.model'
    _description = 'Descripcion'

class Umedida(models.Model):
    _name = 'umedida.model'
    _description = 'Umedida'

class Descripciones(models.Model):
    _name = 'rec.secuencia'
    _description = 'Descripciones'
     
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

class Receta(models.Model):
    _name = 'receta'
    _description = 'Receta'

    temporadas_id = fields.Many2one('cl.product.temporada', string='Temporadas', readonly=False)
    temporada_id = fields.Many2one('temporada.model', string='Temporada', readonly=False)
    secuencia_id = fields.Many2one('secuencia.model', string='Secuencia', readonly=False)
    secuencias_id = fields.Many2one('rec.secuencia', string='Secuencias', readonly=False)
    descripcion_id = fields.Many2one('descripcion.model', string='Descripcion', readonly=True)    
    descripciones_id = fields.Text(string='Descripciones', readonly=True)
    codigosec_id = fields.Many2one('codigosec.model', string='CodigoSec', readonly=False)
    componente_id = fields.Many2one('componente.model', string='Componente', readonly=False)
    descripcion = fields.Text(string='Descripcion', related='componente_id.descripcion', store=False, readonly=True) 
    umedida = fields.Char(string='Umedida', related='componente_id.um', store=False, readonly=True) 
    uni_medida_id = fields.Many2one('unimedida.model', string='UM', readonly=True)
    depto_id = fields.Many2one('depto.model', string='Departamento', readonly=True)
    articulo_id = fields.Many2one('articulo.model', string='Articulo', readonly=False)
    comp_manu_id = fields.Many2one('compmanu.model', string='C/M', readonly=True)
    fact_perdida_id = fields.Float(string='Factor de Perdida (%)', readonly=False)
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

    @api.onchange('componente_id')
    def _onchange_componente_id(self):
        if self.componente_id:
            self.descripcion = self.componente_id.descripcion
        else:
            self.descripcion = ''
