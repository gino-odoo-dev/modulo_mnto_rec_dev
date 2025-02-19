""" # tests/test_receta.py
from odoo.tests.common import TransactionCase

class TestReceta(TransactionCase):
    def setUp(self):
        super(TestReceta, self).setUp()
        self.temporada = self.env['cl.product.temporada'].create({'nombre': 'Temporada 1'})
        self.articulo = self.env['articulo.model'].create({'nombre': 'ArticuloTest123456789012'})
        self.componente = self.env['componente.model'].create({
            'codigo': 'COMP001',
            'descripcion': 'Componente de prueba',
            'um': 'Unidad'
        })

    def test_calcular_costo_ampliado(self):
        receta = self.env['receta'].create({
            'temporadas_id': self.temporada.id,
            'articulo_id': self.articulo.id,
            'componente_id': self.componente.id,
            'cantidad_id': 10,
            'fact_perdida_id': 5.0,
            'c_unitario_id': 100.0,
        })
        self.assertEqual(receta.c_ampliado_id, 50, "El costo ampliado no se calculo correctamente.") """