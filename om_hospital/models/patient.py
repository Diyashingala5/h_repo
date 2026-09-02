from odoo import models, fields,api
 
 
class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  

 
    name = fields.Char(string='Name', default='Hello World!',tracking=True)
    age = fields.Integer(string="Age")
    email=fields.Char(string="Email")
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender')
    weight = fields.Float(string='Weight (kg)')
    is_insured = fields.Boolean(string='Insured')
    notes = fields.Text(string='Notes')
    reference = fields.Char(string="Reference")

    appointments = fields.One2many(
    'hospital.appointment',
    'patient_id',
    string="Appointments"
)


    # Relation fields
    # doctor_id = fields.Many2one('res.partner', string='Doctor')
