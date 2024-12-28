from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle.model.category'

    name = fields.Selection(
            [('car', 'Carro'),
            ('motorcycle', 'Moto'),
            ('truck', 'Camioneta')], string='Categoría', required=True)