from odoo import models, fields, api

class UberRoute(models.Model):
    _name = 'uber.route'
    _description = "Rutas"
    
    origin = fields.Selection([
        ('plaza_venezuela', 'Plaza Venezuela'),
        ('catia', 'Catia'),
        ('la_trinidad', 'La Trinidad'),
        ('petare', 'Petare'),
        ('la_rinconada', 'La Rinconada')], string="Origen", required=True) 
    destination = fields.Selection([
        ('plaza_venezuela', 'Plaza Venezuela'),
        ('catia', 'Catia'),
        ('la_trinidad', 'La Trinidad'),
        ('petare', 'Petare'),
        ('la_rinconada', 'La Rinconada')], string="Destino", required=True) 
    distance = fields.Float("Distancia", compute='_compute_distance')
    cost = fields.Float("Costo", compute='_compute_cost')
    image = fields.Binary(string="Imagen")


    @api.depends('origin', 'destination')
    def _compute_distance(self):
        distances = {
            ('plaza_venezuela', 'catia'): 9.5,
            ('plaza_venezuela', 'la_trinidad'): 12.4,
            ('plaza_venezuela', 'petare'): 10.9,
            ('plaza_venezuela', 'la_rinconada'): 12.7,
            ('catia', 'la_rinconada'): 13.9,
            ('catia', 'plaza_venezuela'): 9.5,
            ('catia', 'petare'): 19.5,
            ('catia', 'la_trinidad'): 20.9,
            ('la_trinidad', 'catia'): 20.9,
            ('la_trinidad', 'petare'): 15.4,
            ('la_trinidad', 'plaza_venezuela'): 12.4,
            ('la_trinidad', 'la_rinconada'): 22.9,
            ('la_rinconada', 'la_trinidad'): 22.9,
            ('la_rinconada', 'catia'): 13.9,
            ('la_rinconada', 'plaza_venezuela'): 12.7,
            ('la_rinconada', 'petare'): 20,
            ('petare', 'la_rinconada'): 20,
            ('petare', 'la_trinidad'): 15.4,
            ('petare', 'catia'): 19.5,
            ('petare', 'plaza_venezuela'): 10.9,
        }

        for record in self:
            key = (record.origin, record.destination)
            record.distance = distances.get(key, 0)

    @api.depends('distance')
    def _compute_cost(self):
        for record in self:
            record.cost = record.distance * 0.60