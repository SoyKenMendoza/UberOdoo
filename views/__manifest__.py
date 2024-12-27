{
    'name': 'Uber',
    'category': 'CursoPRoyecto',
    'version': '16.0.0.0.0',
    'license': 'AGPL-3',
    'author': 'Iciva Technology',
    'depends': [
        'contacts', 'hr', 'website',
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },
    'application': True,
    'installable': True,
}
