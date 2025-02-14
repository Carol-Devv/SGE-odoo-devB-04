# -*- coding: utf-8 -*-

form odoo import models, fields, api

class Alimento(models.Model):
    _name = 'cms_restaurante.alimento' #tabla de datos interna
    _description = 'Alimento'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True help="Introduzca el alimento.")
    quantity = fields.Integer('Cantidad', help="Introduzca la cantidad.")
    category = fields.Selection([
        ('V', 'Vegetal'),
        ('F', 'Fruta'),
        ('C', 'Carne'),
        ('P', 'Pescado'),
        ('L', 'Legumbre'),
        ('DA', 'Derivado animal'),
        ('LA', 'Lácteos'),
        ('FS', 'Frutos secos')
        
    ], string='Categoría')