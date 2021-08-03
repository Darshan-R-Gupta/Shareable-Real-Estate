from django.shortcuts import render
from seller_app.models import *
from .models import *


# Create your views here.

def buyed_share(request):
    buyer_data = {'prop_id': 1, 'buy_share': 5, 'money': 5000000}
    prop = Property.objects.get(id=buyer_data['prop_id'])
    if prop.price_per_share * int(buyer_data['buy_share']) != float(buyer_data['buy_share']):
        print("Locho Che")
    else:
        prop.no_of_shares -= int(buyer_data['buy_share'])
        obj = Buyer.objects.create(
            buyer_details=User.objects.get(pk=request.user.id),
            buyer_property=prop,
            buyer_share=int(buyer_data['buy_share']),
        )
        obj.save()


def buy(request,id):
    prop = Property.objects.filter(id=id)
    print(prop)
    return render(request,'buy.html',{'prop':prop[0]})


def buyer_home(request):
    list_of_prop = Property.objects.filter(no_of_shares__gt = 0)
    return render(request, 'buyer_home.html',{'list':list_of_prop})
