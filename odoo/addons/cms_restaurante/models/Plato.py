# -*- coding: utf-8 -*-

form odoo import models, fields, api

class Plato(models.Model):
    _name = 'cms_restaurante.plato'
    _description = 'Plato'
    
    ###array de alimentos[] ??
    cookingTime = fields.Float('Tiempo de preparación', help="Introduzca el tiempo de preparación.")
    available = fields.Boolean('Disponible')
    