##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools.sql import drop_view_if_exists
import logging

class supplier_category_report(osv.osv):
    _name = 'sale_supplier_category.report'
    _description = 'Sale Supplier Category Name'
    _auto = False
    _order = 'id desc'
    _columns={
        'name_template':fields.text('Name',readonly=True),
        'date_order':fields.date('Order Date',readonly=True),
        'product_uom_qty':fields.float('Quantity',readonly=True),
        'amount_total':fields.float('Total Amount',readonly=True),
        'x_name':fields.text('Supplier Category',readonly=True)
    }

    def init(self,cr):
        drop_view_if_exists(cr,'sale_supplier_category_report')
        cr.execute("""
        create or replace view sale_supplier_category_report AS
        (select row_number() OVER (order by sm.write_date) as id,pp.name_template,
  sm.product_qty as product_uom_qty,sm.create_date as date_order,
  pt.list_price*sm.product_qty as amount_total,spl.name,xpsc.x_name
from stock_move sm inner join product_product pp
    on sm.product_id=pp.id and sm.state='done' AND (sm.location_id=27)
LEFT JOIN
product_template pt on pt.id = pp.product_tmpl_id
  LEFT JOIN
  stock_production_lot spl on spl.id = sm.prodlot_id
  LEFT JOIN
  x_product_supplier_category xpsc on xpsc.id = spl.x_supplier_category)
        """)
    def unlink(self, cr, uid, ids, context=None):
        raise osv.except_osv(_('Error!'), _('You cannot delete any record!'))
supplier_category_report()
