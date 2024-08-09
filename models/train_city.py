# -*- coding: utf-8 -*-
from odoo import models, fields

class TrainCity(models.Model):
    _name = 'train.city'
    _description = 'Train City'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
