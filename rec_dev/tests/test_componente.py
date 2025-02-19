""" # tests/test_componente.py
from odoo.tests.common import TransactionCase

class TestComponente(TransactionCase):
    def setUp(self):
        super(TestComponente, self).setUp()
        self.componente = self.env['componente.model'].create({
            'codigo': 'COMP001',
            'descripcion': 'Componente de prueba',
            'um': 'Unidad'
        })

    def test_onchange_componente_id(self):
        receta = self.env['receta'].new({})
        receta.componente_id = self.componente.id
        receta._onchange_componente_id()
        self.assertEqual(receta.descripcion, 'Componente de prueba', "La descripcion no se actualizó correctamente.")
        self.assertEqual(receta.umedida, 'Unidad', "La unidad de medida no se actualizo correctamente.") """