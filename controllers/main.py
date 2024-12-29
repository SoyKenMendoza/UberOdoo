from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)



class Main(http.Controller):

    @http.route('/trip_selection', type='http', auth="public", website=True)
    def trip_selection(self, **kw):

        return request.render(
            'uber.trip_selection',
            {

            }
        )
    