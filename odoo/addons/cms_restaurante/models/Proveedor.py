# -*- coding: utf-8 -*-

form odoo import models, fields, api

class Proveedor(models.Model):
    _name = 'cms_restaurante.proveedor' #tabla de datos interna
    _description = 'Proveedor'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True help="Introduzca el nombre del proveedor.")
    # alimentos[] los alimentos que provee objetos de tipo alimento
    dateStartAgreemetent = fields.Date('Fecha de inicio de contrato', help="Introduzca la fecha de inicio del contrato.")
    

