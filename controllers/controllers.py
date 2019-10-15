# -*- coding: utf-8 -*-
from odoo import http

from odoo.http import request
class MyaccountAddons(http.Controller):
   @http.route('/my/home', type='http', auth='public', website=True)
   def sale_details(self , **kwargs):
    sale_details = http.request.env['sale.order'].search([])

    return http.request.render('myaccount_addons.portal_my_auctions', {
        'my_details': sale_details})

   @http.route('/my/home', type='http', auth='public', website=True)
   def execute_query(self):
       user = http.request.env.context.get('uid')
       query = "Select (select sum(residual_signed) from account_invoice where partner_id=7 ) as a, (select sum(amount_total_signed) from account_invoice where partner_id=7 ) as b,(select amount from account_payment where partner_id=7 and payment_date=(SELECT MAX(payment_date) FROM account_payment where partner_id=7 and state='posted') ) as c,(select payment_date from account_payment where partner_id=7 and payment_date=(SELECT MAX(payment_date) FROM account_payment where partner_id=7 and state='posted') ) as d"
       request.cr.execute(query)
       companies1 = request.cr.dictfetchall()
       return http.request.render('myaccount_addons.portal_my_auctions', {
           # pass company details to the webpage in a variable
           'companies1': companies1})

   @http.route(['/wallet/balance/confirm'], type='http', auth="public", website=True)
   def wallet_balance_confirm(self, **post):
       product = request.env['product.product'].sudo().search([('name', '=', 'Wallet Recharge')])

       product_id = product.id
       add_qty = 0
       set_qty = 0
       product.update({'lst_price': post['amount']})
       # product.lst_price = post['amount']
       request.website.sale_get_order(force_create=1)._cart_update(
           product_id=int(product_id),
           add_qty=float(add_qty),
           set_qty=float(set_qty),
       )
       return request.redirect("/shop/cart")

   @http.route(['/wallet/balance/Overdue'], type='http', auth="public", website=True)
   def wallet_balance_confirm(self, **post):
       product = request.env['product.product'].sudo().search([('name', '=', 'Wallet Recharge')])

       product_id = product.id
       add_qty = 0
       set_qty = 0
       product.update({'lst_price': post['Overdue']})
       # product.lst_price = post['amount']
       request.website.sale_get_order(force_create=1)._cart_update(
           product_id=int(product_id),
           add_qty=float(add_qty),
           set_qty=float(set_qty),
       )
       return request.redirect("/shop/cart")

 

