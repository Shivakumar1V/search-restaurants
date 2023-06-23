from django.shortcuts import render
from app.models import Restaurant
from django.db.models import Q
import json

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def restaurants(request):
    if request.method == "POST":
        search = request.POST.get('search')
        rest = Restaurant.objects.filter(Q(items__icontains=search))
        rest = rest.order_by('-rating')
        all_rest = []

        for i in rest:
            if i.full_details:
                full_details = json.loads(i.full_details)
                location = full_details.get('location')
                location = f"{location.get('address')}, {location.get('city')}"
                rating = full_details.get('user_rating')
                del_availabilty = full_details.get('has_online_delivery') 
            else:
                location = i.location
                rating =  {'rating_text': 'Unavailable', 'rating_color': '000', 'aggregate_rating': '0'}

            if del_availabilty:
                devlivery = 'Available'
            else: 
                devlivery = 'Unavailable'

            li = [i.id, str(i.name), location, rating.get('rating_text'), rating.get('rating_color'), rating.get('aggregate_rating'), devlivery]
            all_rest.append(li)

        return render(request, 'app/restaurants.html', {'context': all_rest})
            

def restaurantItems(request, pk):
    if request.method == "GET":
        rest = Restaurant.objects.filter(id=pk)
        return render(request, 'app/restaurant_items.html', {'context': json.loads(rest[0].items)})
        