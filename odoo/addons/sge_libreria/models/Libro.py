# -*- coding: utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'
    
    name = fields.Char('Título', required=True)
    precio = fields.Float('Precio')
    currency_id = fields.Many2one('res.currency', string='Modena')
    ejemplares = fields.Integer('Número de ejemplares', help="Número de ejemplares disponibles")
    fecha_compra = fields.Date('Fecha de compra')
    segmano = fields.Boolean('Segunda mano')
    
    categoria_id = fields.Many2one('sge_libreria.categoria', string='Categoría')