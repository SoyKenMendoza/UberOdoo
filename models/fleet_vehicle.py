from odoo import models, fields

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    uber_driver_id = fields.Many2one('hr.employee', string="Chofer", required=True)

    location = fields.Selection([
        ('plaza_venezuela', 'Plaza Venezuela'),
        ('catia', 'Catia'),
        ('la_trinidad', 'La Trinidad'),
        ('petare', 'Petare'),
        ('la_rinconada', 'La Rinconada')], string="Ubicación", required=True) 
    
    image = fields.Binary(string="Imagen")