from django.http import HttpResponse
from django.shortcuts import render, redirect
from sweets.models import Sweet, Order
from django.contrib import messages
from django.db.models import Max, Sum

sweet_category = Sweet.objects.order_by().values('sweet_category').distinct()
sweet_data = Sweet.objects.all()
data = {'sweet_category' : sweet_category,
        'sweet_data': sweet_data}

def homePage(req):
    #Save the order details in database
    if req.method == 'POST':
        #Auto increment the max available order id
        max_id = Order.objects.aggregate(Max('order_id'))
        if max_id['order_id__max'] is None:
            order_id = 1
        else:
            order_id = max_id['order_id__max'] + 1
        
        context={}
        for item in sweet_data:
             if req.POST[item.sweet_name] != '0':
                 #Save template data in model
                 email = req.user
                 order_quan = req.POST[item.sweet_name]
                 sweet_name = item.sweet_name
                 order_val = float(order_quan) * float(item.price)         
                 obj = Order(order_quan = order_quan, sweet_name_id = sweet_name,
                             email = email, order_val = order_val, order_id = order_id)
                 obj.save()
                 context[item.sweet_name]={'order_quan':order_quan, 'sweet_name':sweet_name,'order_val':order_val}
                 
        big_context={'context':context}
        print('big_context',big_context)
        return render(req,'confirm.html',big_context)
    return render(req,'home.html',data)


def orders(req):
    #Fetch order data to show on confirm.html
    order_data = Order.objects.filter(email = req.user)
    order_data_pending = order_data.filter(order_confirmed = False, order_delivered = False)
    order_id_pending = order_data_pending.values('order_id').annotate(total_val=Sum('order_val'))
    order_data_confirmed = order_data.filter(order_confirmed = True, order_delivered = False)
    order_id_confirmed = order_data_confirmed.values('order_id').annotate(total_val=Sum('order_val'))

    order_data_delivered = order_data.filter(order_confirmed = True, order_delivered = True)
    order_id_delivered = order_data_delivered.values('order_id').annotate(total_val=Sum('order_val'))

    #order_id_data = Order.objects.order_by().values('order_id').distinct()
    order_id_data = order_data.values('order_id').annotate(total_val=Sum('order_val'))
    context = {'order_data_pending': order_data_pending,
               'order_data_confirmed': order_data_confirmed,
               'order_data_delivered': order_data_delivered,
               'order_id_pending': order_id_pending,
               'order_id_confirmed': order_id_confirmed,
               'order_id_delivered': order_id_delivered,
               }
    return render(req,'orders.html',context)

def menu(req):
    #Save the order details in database
    if req.method == 'POST':
        #Auto increment the max available order id
        max_id = Order.objects.aggregate(Max('order_id'))
        if max_id['order_id__max'] is None:
            order_id = 1
        else:
            order_id = max_id['order_id__max'] + 1
        
        context={}
        for item in sweet_data:
             if req.POST[item.sweet_name] != '0':
                 #Save template data in model
                 email = req.user
                 order_quan = req.POST[item.sweet_name]
                 sweet_name = item.sweet_name
                 order_val = float(order_quan) * float(item.price)         
                 obj = Order(order_quan = order_quan, sweet_name_id = sweet_name,
                             email = email, order_val = order_val, order_id = order_id)
                 obj.save()
                 context[item.sweet_name]={'order_quan':order_quan, 'sweet_name':sweet_name,'order_val':order_val}
                 
        big_context={'context':context}
        print('big_context',big_context)
        return render(req,'confirm.html',big_context)
    return render(req,'menu.html',data)