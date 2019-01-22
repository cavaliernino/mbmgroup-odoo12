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
           [('new','Borrador'),
            ('sent','Enviada por R3'),
            ('confirmed','Confirmada por MbM'),
            ('process','En proceso de entrega'),
            ('delivered','Entregada'),
            ('invoiced','Factura emitida'),
            ('paid', 'Pagado')],
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

# class portal_oc(models.Model):
#     _name = 'portal_oc.portal_oc'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100