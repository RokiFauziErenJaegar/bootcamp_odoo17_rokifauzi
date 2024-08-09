# -*- coding: utf-8 -*-
from odoo import models, fields

class TrainStation(models.Model):
    _name = 'train.station'
    _description = 'Train Station'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    city_id = fields.Many2one('train.city', string='City', required=True)
    address = fields.Text()
