# -*- coding: utf-8 -*-

from odoo import models, fields, api


class recordpu3(models.Model):
     _name = 'py3by.recordpu3'
     _description = 'py3by.recordpu3'

     first_name = fields.Char()
     second_name = fields.Char()
     family_name = fields.Char()
     person_id = fields.Char()

     value = fields.Integer()
     #test py 7 j

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
"""
     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
"""
