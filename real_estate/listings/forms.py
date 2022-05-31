from django.forms import ModelForm
from .views import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title", 
            "price",
            "num_bedrooms",
            "square_footage",
            "address",
        ]