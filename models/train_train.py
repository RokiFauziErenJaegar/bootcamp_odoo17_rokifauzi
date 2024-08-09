# -*- coding: utf-8 -*-
from odoo import models, fields

class TrainTrain(models.Model):
    _name = 'train.train'
    _description = 'Train'

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    capacity = fields.Integer()
    state = fields.Selection([
        ('ready', 'Ready'),
        ('not_ready', 'Not Ready'),
        ('maintenance', 'Maintenance')
    ], default='ready')
    active = fields.Boolean(default=True)
    schedule_line_ids = fields.One2many('train.schedule', 'train_id', string='Schedule Lines')
