# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Categoria(models.Model):
    _name = 'sge_libreria.categoria' # crm.lead,    res.partner
    _description = 'Categoría'       # Iniciativa,  Contacto

    name = fields.Char('Nombre', required=True, help="Introduzca nombre de categoría")
    description = fields.Char('Descripción')
    
    libro_ids = fields.One2many('sge_libreria.libro', 'categoria_id', string='Libros')