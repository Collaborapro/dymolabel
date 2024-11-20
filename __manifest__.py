# -*- coding: utf-8 -*-
##############################################################################
#
#    Global Creative Concepts Tech Co Ltd.
#    Copyright (C) 2018-TODAY iWesabe (<http://www.iwesabe.com>).
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Print Product Label Picking',
    'version': '16.0.0.0',
    'author': 'iWesabe',
    'summary': 'Print Product Label From Picking',
    'description': """This module helps to print product label from picking.""",
    'category': 'Products',
    'website': 'https://www.iwesabe.com/',
    'license': 'LGPL-3',
    'depends': ['stock','purchase','product'],
    'data': [
        'security/ir.model.access.csv',
        'report/picking_product_label.xml',
        'wizard/picking_product_label_wizard_views.xml',
    ],
    'qweb': [],
    'images': ['static/description/iWesabe-Apps-Product-Label.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
