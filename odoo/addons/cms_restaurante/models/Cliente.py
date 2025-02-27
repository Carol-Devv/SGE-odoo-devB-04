# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'cms_restaurante.cliente' #tabla de datos interna
    _description = 'Cliente'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del cliente.") #nombre del cliente
    
    # platos[] los platos que compra objetos de tipo plato dish: relación    cliente : plato     N cliente N platos      cliente N : M platos
    dish_ids = fields.Many2many('cms_restaurante.plato', string='Platos', relation='cms_restaurante_cliente_plato_rel') #platos que pide el cliente
    
    costOrder = fields.Float('Precio', help="Sumatorio de los pedidos") #campo calculado --> sumatorio del precio de cada plato que se pide
    dateOrder = fields.Date('Fecha de compra del pedido', help="Introduzca la fecha de compra del pedido.") # fecha del pedido