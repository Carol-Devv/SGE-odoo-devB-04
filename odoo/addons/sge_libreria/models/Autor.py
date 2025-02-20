# -*- coding: utf-8 -*-

from odoo import models, fields

class Autor(models.Model):
    _name = 'sge_libreria.autor'
    _description = 'Autor'

    name = fields.Char('Nombre')
    fecha_nac = fields.Date('Fecha de nacimiento')
    country_id = fields.Many2one('res.country', string="País de origen")
    
    ###libro_ids = fields.Many2many('sge_libreria.libro', string='Libros', relation='sge_libreria_libro_autor_rel')
