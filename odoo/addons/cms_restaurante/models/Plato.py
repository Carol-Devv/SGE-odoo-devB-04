# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Plato(models.Model):
    _name = 'cms_restaurante.plato'
    _description = 'Plato'
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del plato.") #nombre del plato
    
    cost = fields.Monetary(string='Precio', currency_field='moneda_id')#precio del plato
    moneda_id = fields.Many2one('res.currency', string='Moneda')
    
    cookingTime = fields.Float('Tiempo de preparación', help="Introduzca el tiempo de preparación.") #tiempo de preparación
    available = fields.Boolean('Disponible') # campo calculado según nombre y cantidad de alimentos necesarios
    
    
    # nombre y cantidad alimentos -- > alimento --> relación      plato N : M alimento
    cliente_ids = fields.Many2many('cms_restaurante.cliente', string='Clientes', relation='cms_restaurante_cliente_plato_rel') #registro de clientes
    
    
    alimento_ids = fields.Many2many('cms_restaurante.alimento', string='Alimentos', relation='cms_restaurante_alimento_plato_rel') #alimentos del plato no calculado

    @api.onchange('alimento_ids')
    def _onchange_alimento_ids(self):
        if self.alimento_ids:
            # Inicializa la cantidad de alimentos a 0
            for alimento in self.alimento_ids:
                alimento.cantidad_plato = 0  # Inicializa la cantidad a 0 para cada alimento seleccionado