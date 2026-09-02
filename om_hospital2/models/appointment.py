from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id' 


    reference = fields.Char(
        string="Appointment Reference",
        readonly=True,
        copy=False,
        default="New"
    )

    # Patient Relation
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        tracking=True
    )

    doctor_id = fields.Many2one(
        'res.partner',
        string='Doctor'
    )

    appointment_date = fields.Date(string="Appointment Date", required=True)
    appointment_time = fields.Float(string="Appointment Time")

    reason = fields.Char(string="Reason for Visit")

    # Status
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled')
        ],
        string="Status",
        default='draft',
        tracking=True
    )

    notes = fields.Text(string='Doctor Notes')
    fee = fields.Float(string="Consultation Fee")
    follow_up_date = fields.Date(string="Follow Up Date")
    reference = fields.Char(
    string="Reference",
    default="New",
    readonly=True,
    copy=False
    )

    @api.model
    def create(self, vals):
        print(".........................",vals)
        if vals.get('reference', 'New') == 'New':
          vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals)