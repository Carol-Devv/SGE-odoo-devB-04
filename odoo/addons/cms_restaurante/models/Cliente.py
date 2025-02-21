# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'cms_restaurante.cliente' #tabla de datos interna
    _description = 'Cliente'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del cliente.")
    
    # platos[] los platos que compra objetos de tipo plato dish: relación    cliente : plato     1 cliente N platos      cliente N : 1 platos
    field_name_ids = fields.One2many('cms_restaurante.plato', 'inverse_field_name', string='field_name')
    
    costOrder = fields.Float('Precio', , help="Sumatorio de los pedidos") #campo calculado
    dateOrder = fields.Date('Fecha de compra del pedido', help="Introduzca la fecha de compra del pedido.")