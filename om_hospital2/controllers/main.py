from odoo import http
from odoo.http import request

class HospitalController(http.Controller):

    @http.route('/patients', auth='public', website=True)
    def patients(self):
        patients = request.env['hospital.patient'].sudo().search([])

        return request.render('om_hospital.patient_template', {
            'patients': patients
        })