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
   def navigate_to_detail_page(self):
        # This will get all company details (in case of multicompany this are multiple records)
        result = http.request.env['account.invoice'].sudo().search([])
        companies=sum(result.residual_signed)
        return http.request.render('myaccount_addons.portal_my_auctions', {
          # pass company details to the webpage in a variable
        'companies': companies})

   @http.route('/my/home', type='http', auth='public', website=True)
   def get_last_payment(self, **kwargs):
        partner = http.request.env.context.get('uid')
        payments_ids = http.request.env['account.payment'].search(
               [('partner_id', '=', 7), ('state', '=', 'posted')])
        payment = payments_ids and max(payments_ids)
        return http.request.render('myaccount_addons.portal_my_auctions', {
               # pass company details to the webpage in a variable
               'payment': payment})

   @http.route('/my/home', type='http', auth='public', website=True)
   def execute_query(self):
       user = http.request.env.context.get('uid')
       query = "select sum(residual_signed),sum(amount_total_signed) as total from account_invoice where partner_id=7"
       request.cr.execute(query)
       companies1 = request.cr.dictfetchall()
       return http.request.render('myaccount_addons.portal_my_auctions', {
           # pass company details to the webpage in a variable 
           'companies1': companies1})

   @http.route('/my/home', type='http', auth='public', website=True)
   def execute_query_maxi(self):
       user = http.request.env.context.get('uid')
       query = "select * from account_payment where state='posted' and T.payment_date =( SELECT MAX(payment_date) FROM account_payment) and partner_id=7"
       request.cr.execute(query)
       payment = request.cr.dictfetchall()
       return http.request.render('myaccount_addons.portal_my_auctions', {
           # pass company details to the webpage in a variable
           'payment': payment})
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
# class MyaccountAddons(http.Controller):
#     @http.route('/myaccount_addons/myaccount_addons/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myaccount_addons/myaccount_addons/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myaccount_addons.listing', {
#             'root': '/myaccount_addons/myaccount_addons',
#             'objects': http.request.env['myaccount_addons.myaccount_addons'].search([]),
#         })

#     @http.route('/myaccount_addons/myaccount_addons/objects/<model("myaccount_addons.myaccount_addons"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myaccount_addons.object', {
#             'object': obj
#         })