from django.conf.urls.defaults import *

urlpatterns = patterns('order_export.views',
    (r'^new_orders.csv$', 'admin_order_export', {'status':'New'}, 'admin_new_order_export'),
    (r'^all_orders.csv$', 'admin_order_export', {}, 'admin_all_order_export'),
)
