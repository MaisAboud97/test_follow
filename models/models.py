# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ResPartner(models.Model):
    _inherit = "res.partner"

    # reconciliation
    def action_bank_reconcile_bank_statements(self):
        self.ensure_one()
        partner_id= [self.id]
        return {
            "type": "ir.actions.client",
            "tag": "manual_reconciliation_view",
            "context": {
                'mode': 'customers',
                'partner_ids': partner_id,
                 'all_entries': True ,
            },
        }
    # Send mail automatically (auto excute)
    def _auto_excute(self):
        a = self.env['res.partner'].search([])
        for res in a:
            if res.latest_followup_level_id and  res.latest_followup_level_id.auto_execute:
                res.do_partner_mail()
    # Send activity automatically (auto excute)
    def _send_activity(self):
        mod=self.env['ir.model'].search([('model', '=', 'res.partner')]).id
        follow_state = self.env['followup.stat.by.partner'].search([])
        for rec in follow_state:
            print("aaffffff",rec.partner_id)
            print("aaffffff",rec.date_followup)
            print("alllll",rec.max_followup_id.manual_action)
            if rec.max_followup_id.manual_action :
                action_type = rec.max_followup_id.manual_action_type_id
                res= rec.partner_id
                user= rec.max_followup_id.manual_action_responsible_id
                summary= rec.max_followup_id.manual_action_note
                date= rec.date_followup
                vals={'res_id':res,'activity_type_id':action_type.id,'user_id':user.id,'res_model_id':mod,'summary':summary, 'date_deadline':date}
                new = rec.env['mail.activity'].create(vals)
                return new
            
class AcccountFollowUp(models.Model):
    _inherit ='followup.line'

        
    manual_action_type_id = fields.Many2one('mail.activity.type', 'Manual Action Type', default=False)
    auto_execute = fields.Boolean(string="Auto excute")

    # don't need manual action if we use auto excute 
    @api.onchange('auto_execute')
    def _get_auto(self):
        for rec in self:
            if rec.auto_execute :
                rec.manual_action = False

    

