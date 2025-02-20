# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'cms_restaurante.cliente' #tabla de datos interna
    _description = 'Cliente'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del cliente.")
    # platos[] los platos que compra objetos de tipo plato dish
    dateOrder = fields.Date('Fecha de compra del pedido', help="Introduzca la fecha de compra del pedido.")