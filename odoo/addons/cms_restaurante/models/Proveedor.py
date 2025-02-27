# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Proveedor(models.Model):
    _name = 'cms_restaurante.proveedor' #tabla de datos interna
    _description = 'Proveedor'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True, help="Introduzca el nombre del proveedor.") #Nombre del proveedor
    
    # alimentos[] los alimentos que provee objetos de tipo alimento
    alimento_ids = fields.One2many('cms_restaurante.alimento', 'proveedor_id', string='Ingredientes')
    
    #campo único porque se repetirá el nombre del proveedor para añadir cantidad de producto
    # fecha de venta alimentos
    dateStartAgreemetent = fields.Date('Fecha de inicio de contrato', required=True, help="Introduzca la fecha de inicio del contrato.") 
    

