# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request


class newMyaccountAddons(http.Controller):

    @http.route('/my/home', type='http', auth='public', website=True)
    def execute_query1(self):
        user = http.request.env.context.get('uid')
        query = "select * from account_payment where partner_id=7"
        request.cr.execute(query)
        payment = request.cr.dictfetchall()
        return http.request.render('myaccount_addons.portal_my_auctions', {
           'payment': payment})

