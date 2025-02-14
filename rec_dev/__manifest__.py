{
    'name': 'Ficha Tecnica',
    'version': '1.0',
    'summary': 'Modulo mantenimiento ficha tecnica creacion de recetas',
    'description': 'Mantenimiento Ficha Tecnica.',
    'author': 'MarcoAG',
    'depends': ['base', 'web'],
    'data': [
        'views/rec_model_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'rec_dev/static/src/css/styles.css',
            'rec_dev/static/src/js/remove_tr.js',
        ],
    },
    'installable': True,
    'application': True,
}
