# -*- coding: utf-8 -*-

from odoo import models, fields

class PlatoAlimento(models.Model):
    _name = 'cms_restaurante.plato_alimento'
    _description = 'Cantidad de Alimento para un Plato'

    plato_id = fields.Many2one('cms_restaurante.plato', string='Plato', required=True)
    alimento_id = fields.Many2one('cms_restaurante.alimento', string='Alimento', required=True)
    quantity_ingredient = fields.Integer('Cantidad', required=True, help="Cantidad del alimento necesaria para el plato.")