# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plato(models.Model):
    _name = 'cms_restaurante.plato'
    _description = 'Plato'
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del plato.")
    # nombre y cantidad alimentos -- > alimento --> relación      plato N : M alimento
    cookingTime = fields.Float('Tiempo de preparación', help="Introduzca el tiempo de preparación.")
    available = fields.Boolean('Disponible') # campo calculado según nombre y cantidad de alimentos necesarios
    
    cliente_id = fields.Many2one('cms_restaurante.cliente', string='Clientes')
     