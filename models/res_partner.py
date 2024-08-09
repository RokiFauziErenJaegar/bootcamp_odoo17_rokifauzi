# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    train_state = fields.Selection([
        ('passenger', 'Passenger'),
        ('machinist', 'Machinist')
    ])
    identity = fields.Char(string='Identity Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ])
    born_date = fields.Date()

    @api.onchange('train_state')
    def _onchange_train_state(self):
        if self.train_state:
            self.identity = self.identity or False
            self.gender = self.gender or False
            self.born_date = self.born_date or False
        else:
            self.identity = False
            self.gender = False
            self.born_date = False
