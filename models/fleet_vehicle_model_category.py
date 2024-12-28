from odoo import models, fields

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    name = fields.Selection(
            [('car', 'Carro'),
            ('motorcycle', 'Moto'),
            ('truck', 'Camioneta')], string='Categoría', required=True)