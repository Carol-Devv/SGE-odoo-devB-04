# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alimento(models.Model):
    _name = 'cms_restaurante.alimento' #tabla de datos interna
    _description = 'Alimento'          #lo ve el usuario usuario
    
    name = fields.Char('Nombre', required=True, help="Introduzca el alimento.") #nombre del alimento
    quantity = fields.Integer('Cantidad', help="Introduzca la cantidad.") #calculado según pidan platos y vendan proveedores
    
    #tipos de alimentos
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
    
    # nombre proveedor --> relación    proveedor 1 : N alimento
    proveedor_id = fields.Many2one('cms_restaurante.proveedor', string='Proveedor')
    
    # nombre platos en los que está --> relación   plato N : M alimento
    plato_ids = fields.Many2many('cms_restaurante.plato', string='Platos', relation='cms_restaurante_alimento_plato_rel', compute='_compute_plato_ids', store=False)
    
    @api.depends('name')  # name de alimento
    def _compute_plato_ids(self):
        for alimento in self:
            platos = self.env['cms_restaurante.plato'].search([('alimento_ids', 'in', alimento.id)])
            alimento.plato_ids = platos
    

    
    
    
   