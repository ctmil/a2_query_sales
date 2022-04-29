from odoo import tools, models, fields, api, _

class A2Sales(models.Model):
    _name = "a2.sales"
    _description = "A2 Sales"
    _auto = False

    partner_id = fields.Many2one('res.partner','Cliente')
    city = fields.Char('Ciudad')
    state_id = fields.Many2one('res.country.state','Provincia')
    product_id = fields.Many2one('product.product','Producto')
    product_uom_qty = fields.Float('Cantidad')

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        query = """
            select sol.id,so.partner_id,pa.city,pa.state_id,sol.product_id,sol.product_uom_qty
            from sale_order_line sol
            inner join sale_order so on so.id = sol.order_id
            inner join res_partner pa on pa.id = so.partner_id
            """
        self._cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, query))
