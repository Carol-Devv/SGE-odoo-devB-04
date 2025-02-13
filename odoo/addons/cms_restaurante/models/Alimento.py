# -*- coding: utf-8 -*-

form odoo import models, fields, api

class Alimento(models.Model):
    _name = 'cms_restaurante.alimento' #tabla de datos interna
    _description = 'Alimento'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True help="Introduzca el alimento.")
    field_name = fields.Integer('Cantidad', help="Introduzca la cantidad.")
    # ver que hago con las keys y en qué orden los muestro?? se muestran?? no sé
    field_name = fields.Selection([
        ('V', 'Vegetal'),
        ('F', 'Fruta'),
        ('C', 'Carne'),
        ('P', 'Pescado'),
        ('L', 'Legumbre'),
        ('DA', 'Derivado animal'),
        ('LA', 'Lácteos'),
        ('FS', 'Frutos secos')
        
    ], string='field_name')