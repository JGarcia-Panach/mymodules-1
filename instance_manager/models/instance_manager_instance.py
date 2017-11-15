# Copyright (C) 2017 Creu Blanca
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models
class Instance(models.Model):
    #Attributes
    _name = 'instance.manager.instance'
    _order = 'client'

    #Fields
    client = fields.Many2one('instance.manager.client','Client')
    ip = fields.Char('IP',15)
    version = fields.selection()
    domains = fields.One2many('modelo','campo','Domain')
    machine = fields.Char('Machine')
    state = fields.Boolean('State')
    backEndLogin = fields.Many2one('instance.manager.login','BackEnd Login')
    postgresqlLogin = fields.Many2one('instance.manager.login','Postgresql Login')
    sshLogin = fields.Many2one('instance.manager.loggin','SSH Login')
    #repositories = campo calculado?
    modules = fields.Many2many('instance.manager.module','Modules')
