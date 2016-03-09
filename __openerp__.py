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
{
    "name":"Bahmni Custom",
    "version":"1.0",
    "author":"Sandeep, ThoughtWorks Technologies Pvt. Ltd.",
    "category":"PossibleCustom",
    "description":"Custom changes for possible environment",
    "depends": ["base","bahmni_internal_stock_move","bahmni_pharmacy_product","bahmni_purchase_extension","stock","purchase","account","web_d3_chart"],
    'data':['module_misc.xml','purchase_by_supplier_category_view.xml','sale_by_supplier_category_view.xml','moving_inventory_analysis.xml','stock_out_report.xml','min_max_report.xml'],
    'demo':[],
    'auto_install':False,
    'application':True,
    'installable':True,
}
