# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"


    marital_status = fields.Selection([('solteiro', 'solteiro(a)'), ('uniao', 'em união estavel'),
                              ('casado', 'casado(a)'), ('divorciado', 'divorciado(a)'),
                              ('viuvo', 'viúvo(a)'),
                              ('separado', 'separado(a)')],
                             default='solteiro',
                             string='Estado Cívil')
