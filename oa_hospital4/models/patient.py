# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    ref = fields.Char(string='Reference', tracking=True)
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string="Appointments")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag' , string="Tags")
    appointment_count = fields.Integer(string="Appointment Count")



    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)
    # yukarıdaki yaptığımız tanımlamayla 'patient' menüsünde yeni bir hasta kaydı oluşturup,
    # kaydettiğimizde,(create metodu için) 'ref' alanı otomatik olarak "OA------" olarak doldurulacak

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)
    # Patient menüsündeki, herhangi bir kayıt üzerinde değişiklik yapıldığında çalışıyor.

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1


    def name_get(self):
        return[(record.id, "%s [%s]" % (record.name, record.ref)) for record in self]