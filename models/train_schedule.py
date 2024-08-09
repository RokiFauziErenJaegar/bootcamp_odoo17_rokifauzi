# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.fields import Datetime

class TrainSchedule(models.Model):
    _name = 'train.schedule'
    _description = 'Train Schedule'

    code = fields.Char(readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('train.schedule'))
    origin_id = fields.Many2one('train.station', string='Origin', required=True)
    destination_id = fields.Many2one('train.station', string='Destination', required=True)
    schedule_time = fields.Datetime(required=True)
    duration = fields.Float()
    arrival_time = fields.Datetime(compute='_compute_arrival_time')
    train_id = fields.Many2one('train.train', string='Train', required=True)
    capacity = fields.Integer(related='train_id.capacity')

    @api.depends('schedule_time', 'duration')
    def _compute_arrival_time(self):
        for record in self:
            if record.schedule_time and record.duration:
                record.arrival_time = Datetime.add(record.schedule_time, hours=record.duration)
