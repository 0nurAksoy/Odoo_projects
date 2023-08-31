# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    cancel_days = fields.Integer(string='Cancel Days', config_parameter="oa_hospital5.cancel_days")
