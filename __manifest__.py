{
    'name': 'Uber',
    'category': 'CursoPRoyecto',
    'version': '16.0.0.0.0',
    'license': 'AGPL-3',
    'author': 'Iciva Technology',
    'depends': [
        'contacts', 'hr', 'fleet', 'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/uber_route_views.xml',
        'views/uber_menu.xml',
        'views/fleet_vehicle_views.xml',        

    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },
    'application': True,
    'installable': True,
}
