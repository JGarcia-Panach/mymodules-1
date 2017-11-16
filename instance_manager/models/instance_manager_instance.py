# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models
class Instance(models.Model):
    #Attributes
    _name = 'instance.manager.instance'
    _order = 'client'

    #Fields
    res_partner_id = fields.Many2one('res.partner','Client')
    ip = fields.Char('IP',15)
    version = fields.selection([('8.0','8.0'),('9.0','9.0'),('10.0','10.0'),('11.0','11.0')],'Version')
    domain_ids = fields.Text('','Domains')
    machine = fields.Char('Machine')
    state = fields.Boolean('State')
    description = fields.Text('','Description');
    backEndUser = fields.Char('User')
    backEndPass = fields.Char('Pass')
    postgreUser = fields.Char('User')
    postgrePass = fields.Char('Pass')
    sshUser = fields.Char('User')
    sshPass = fields.Char('Pass')
    #repositories = fields.Many2many('instance.manager.repository','Modules')
    #modules = fields.Many2many('instance.manager.module','Modules')
