# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TrainScheduleWizard(models.TransientModel):
    _name = 'train.schedule.wizard'
    _description = 'Train Schedule Wizard'

    train_id = fields.Many2one('train.train', string='Train', required=True)
    schedules = fields.One2many('train.schedule.line', 'wizard_id', string='Schedules')

    def create_schedules(self):
        schedule_obj = self.env['train.schedule']
        for line in self.schedules:
            schedule_obj.create({
                'train_id': self.train_id.id,
                'origin_id': line.origin_id.id,
                'destination_id': line.destination_id.id,
                'schedule_time': line.schedule_time,
                'duration': line.duration,
            })

class TrainScheduleLine(models.TransientModel):
    _name = 'train.schedule.line'
    _description = 'Train Schedule Line'

    wizard_id = fields.Many2one('train.schedule.wizard', string='Wizard Reference')
    origin_id = fields.Many2one('train.station', string='Origin', required=True)
    destination_id = fields.Many2one('train.station', string='Destination', required=True)
    schedule_time = fields.Datetime(string='Schedule Time', required=True)
    duration = fields.Float(string='Duration', required=True)
