from django.shortcuts import render
from property.models import * 

# Create your views here.
def search_with_map(request): 
    apartments_rent = ApartmentRent.objects.all() 
    floors_rent = FloorRent.objects.all() 
    villas_rent = VillaRent.objects.all() 
    shops_rent = ShopRent.objects.all() 
    resthouses_rent = RestHouseRent.objects.all() 
    commercial_offices_rent = CommercialOfficeRent.objects.all() 
    lands_rent = LandRent.objects.all() 
    buildings_rent = BuildingRent.objects.all() 
    warehouses_rent = WarehouseRent.objects.all() 
    furnished_apartements_rent = FurnishedApartmentRent.objects.all() 
    chalets_rent = ChaletRent.objects.all() 


    context = {
        'apartments_rent': apartments_rent,
        'floors_rent': floors_rent, 
        'villas_rent': villas_rent, 
        'shops_rent': shops_rent, 
        'resthouses_rent': resthouses_rent, 
        'commercial_offices_rent': commercial_offices_rent, 
        'lands_rent': lands_rent, 
        'buildings_rent': buildings_rent, 
        'warehouses_rent': warehouses_rent, 
        'furnished_apartements_rent': furnished_apartements_rent, 
        'chalets_rent': chalets_rent 
    } 

    return render(request, 'maps/index.html', context)


# let apartments_rent_data = []; 
# let floors_rent_data = []; 
# let villas_rent_data = []; 
# let shops_rent_data = [] ; 
# let resthouses_rent_data = []; 
# let commercial_offices_rent_data = []; 
# let lands_rent_data = []; 
# let buildings_rent_data = []; 
# let warehouses_rent_data = [] ; 
# let furnished_apartements_rent_data =[]; 
# let chalets_rent_data = []; 
