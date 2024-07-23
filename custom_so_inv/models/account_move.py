# Part of kobros-tech. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_children_ids = fields.One2many(related="partner_id.child_ids")

    kind_attention = fields.Many2one(
        comodel_name='res.partner',
        string="Kind Attention",
        domain="[('id', 'in', partner_children_ids)]",
    )

    message = fields.Html(
        string='Welcome message',
        default="Dear Sir, You are kindly requested to process the due amount as stated below:",
    )
    