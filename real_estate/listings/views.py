from django.shortcuts import render
from .models import Listing

# Create your views here.



def listing_list(request, *args, **kwargs):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


def listing_retrieve(request, id, *args, **kwargs):
    listing = Listing.objects.get(id=id)
    context = {
        "listing": listing
    }
    return render(request, "retrieve_listing.html", context)