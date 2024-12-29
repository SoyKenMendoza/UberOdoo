from odoo import http
from odoo.http import request
import logging

class Main(http.Controller):

    @http.route('/trip_selection', type='http', auth="public", website=True)
    def trip_selection(self, **kw):

        return request.render(
            'UberOdoo.trip_selection',
            {

            }
        )
    