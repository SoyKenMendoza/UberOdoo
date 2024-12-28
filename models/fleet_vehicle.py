from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    uber_driver_id = fields.Many2one('hr.employee', string="Chofer", required=True)