# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MbMStage(models.Model):
    _name = 'portal_oc.stage'
    _description = 'MbM Stage'
    _order = 'sequence,name'
    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new','New'),
        ('open','Open'),
        ('done','Paid'),
        ('cancel','Cancelled')],
        default='new',
    )
class PurchaseOrderMbM(models.Model):
    _inherit = 'purchase.order'
    @api.model
    def _default_stage(self):
        Stage = self.env['portal_oc.stage']
        return Stage.search([], limit=1)
    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)
    stage_id = fields.Many2one(
        'portal_oc.MbMStage',
        default=_default_stage,
        group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state')
    #@api.on_change('stage_id')
    #def onchange_stage_id(self):
    #    if self.stage_id.sequence == 20:
    #        #create sales order with data

class SaleOrderMbM(models.Model):
    _inherit = 'sale.order'
    @api.model
    def _default_stage(self):
        Stage = self.env['portal_oc.stage']
        return Stage.search([], limit=1)
    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)
    stage_id = fields.Many2one(
        'portal_oc.MbMStage',
        default=_default_stage,
        group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state')

# class portal_oc(models.Model):
#     _name = 'portal_oc.portal_oc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 10#0