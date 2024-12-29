{
    'name': 'uber',
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
        'views/fleet_vehicle_views.xml',
        'views/trip_selection.xml', 
        'views/uber_menu.xml',
        'data/res_partner_data.xml',       
    ],
    'assets': {
        'web.assets_frontend': [
            'UberOdoo/static/src/**/*',
        ],
    },
    'application': True,
    'installable': True,
}
