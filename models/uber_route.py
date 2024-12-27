from odoo import models, fields

class UberRoute(models.Model):
    _name = 'uber.route'
    _description = "Rutas"
    
    origin = fields.Char("Origen", required=True)
    destination = fields.Char("Destino", required=True)
    distance = fields.Float("Distancia", required=True)
    cost = fields.Float("Coste", required=True)
    image = fields.Binary(string="Imagen")
