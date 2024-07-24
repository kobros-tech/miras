# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#############################################################################
#
#    kobros-tech Pvt. Ltd.
#
#    Copyright (C) 2020-TODAY kobros-tech(<https://www.linkedin.com/company/kobros-tech/>).
#    Author: Mohamed Alkobrosli(<https://www.linkedin.com/in/mohamed-alkobrosly/>)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Custom module for Miras Invoice & Sale addons",
    'description': """
        Custom module for Miras Invoice & Sale addons that modifies some fileds and updates their reports.
    """,
    'author': 'Abou Sajid (Mohamed Alkobrosli)',
    'company': 'kobros-tech',
    'maintainer': 'Mohamed Moustafa Alkobrosli',
    'website': "https://www.kobros-tech.com",
    'license': "AGPL-3",
    'depends': ['sale_management', 'account', 'account_accountant'],
    'data': [
        "views/sale_order_views.xml",
        "views/account_move_views.xml",

        "report/report_templates.xml",
        "report/ir_actions_report_templates.xml",
        "report/ir_actions_report.xml",
    ],
}
