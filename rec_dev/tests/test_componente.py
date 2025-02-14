# tests/test_componente.py
from odoo.tests.common import TransactionCase

class TestComponente(TransactionCase):
    def setUp(self):
        super(TestComponente, self).setUp()
        # Crear un componente para las pruebas
        self.componente = self.env['componente.model'].create({
            'codigo': 'COMP001',
            'descripcion': 'Componente de prueba',
            'um': 'Unidad'
        })

    def test_onchange_componente_id(self):
        # Verificar la formula onchange 
        receta = self.env['receta'].new({})
        receta.componente_id = self.componente.id
        receta._onchange_componente_id()
        # Verificar que se actualicen los modelos 
        self.assertEqual(receta.descripcion, 'Componente de prueba', "La descripcion no se actualizó correctamente.")
        self.assertEqual(receta.umedida, 'Unidad', "La unidad de medida no se actualizo correctamente.")