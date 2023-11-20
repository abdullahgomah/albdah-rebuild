from django.shortcuts import render, redirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .models import * 
from accounts.models import Favourite
import uuid 
import os 


# Create your views here.


@login_required(login_url='/auth/')
def add_property_interface(request):
    context = {} 
    return render(request, 'property/add-property-interface.html', context)


def property_details(request, number): 
    property = Property.objects.get(number = number) 
    context = {
        'property': property, 
    } 
    return render(request, 'property/property-details.html', context ) 

@login_required(login_url='/auth/')
def add_property(request, property_type): 

    
    if request.POST: 

        user = request.user 
        # GENERAL FIELDS 
        sale = request.POST.get("sale") 
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        neighborhood = request.POST.get('neighborhood-input')
        city = request.POST.get('city-input')
        price = request.POST.get('price-input') 
        space = request.POST.get('space-input')
        advertiser_relation = request.POST.get('advertiser_relation')
        exclusive = request.POST.get('exclusive')
        if advertiser_relation != "مسوق": 
            exclusive = 0  
        else: 
            exclusive = request.POST.get('exclusive') 
        
        video = request.FILES.get('property__video')
        unique_filename = str(uuid.uuid4()) 
        _, file_extension = os.path.splitext(video.name)
        new_filename = f"{unique_filename}{file_extension}"


        with open(os.path.join('media', new_filename), 'wb+') as destination:
            for chunk in video.chunks():
                destination.write(chunk)


        street_width = request.POST.get('street-width-input') 
        property_age = request.POST.get('extra-property-age-input') 
        if property_age == None or property_age == '' or property_age == 0: 
                property_age = request.POST.get('property-age-input') 
            
        rent_type = request.POST.get('rent_type_input')
        description = request.POST.get('property__description__input')
        water_exist = request.POST.get('water_exist')
        power_exist = request.POST.get('power_exist')
        sanitation_exist = request.POST.get('sanitation_exist')
        images = request.FILES.getlist('property__imgs') 
        images_status = request.POST.getlist('mainImage') 

        rooms = request.POST.get('extra-room-input') 
        if rooms == None or rooms == "" or rooms == 0: 
            rooms = request.POST.get("room-input")  
        
        
        lounges = request.POST.get('extra-lounges-input') 
        if lounges == None or lounges == "" or lounges == 0: 
            lounges = request.POST.get('lounges-input') 
        

        bathrooms = request.POST.get('extra-bathroom-input') 
        if bathrooms == None or bathrooms == '' or bathrooms == 0 : 
            bathrooms = request.POST.get('bathroom-input') 


        features = [
            water_exist,
            power_exist, 
            sanitation_exist, 
        ]


        if property_type == 'apartment_rent' or property_type == 'floor_rent' or property_type == 'apartment_sale' or property_type == 'floor_sale': 


            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 


            families = request.POST.get('families') 
            furnished = request.POST.get('furnished') 
            kitchen = request.POST.get('kitchen') 
            extenstion = request.POST.get('extenstion') 
            car_entrance = request.POST.get('car_entrance') 
            elevator = request.POST.get('elevator') 
            ac = request.POST.get('ac') 
            private_surface = request.POST.get('private_surface') 
            in_villa = request.POST.get('in_villa') 
            two_enternace = request.POST.get('two_enternace') 
            private_enternace = request.POST.get('private_enternace') 
            
            features.append(families) # 3
            features.append(furnished) # 4
            features.append(kitchen) # 5
            features.append(extenstion) # 6 
            features.append(car_entrance) # 7
            features.append(elevator) # 8 
            features.append(ac) # 9 
            features.append(private_surface) # 10 
            features.append(in_villa) # 11 
            features.append(two_enternace) # 12 
            features.append(private_enternace) # 13 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create(
                user= user, 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = new_filename, 
                # interface= interface, 
                # stores_count = stores_count, 
                # apartments_count = apartments_count, 
                street_width = street_width, 
                rooms = rooms , 
                lounges = lounges, 
                bathroom = bathrooms, 
                floor =floor, 
                property_age = property_age, 
                # family_part = family_part, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                furnished = features[4], 
                kitchen = features[5], 
                extenstion = features[6], 
                car_entrance = features[7], 
                elevator = features[8], 
                ac = features[9], 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2], 
                private_enternace = features[13], 
                lat = lat, 
                lng = lng  
        )

        
        elif property_type == 'shop_rent': 
            interface = request.POST.get('interface-input') 
            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 


            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create(
                user = user, 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                interface= interface, 
                # stores_count = stores_count, 
                # apartments_count = apartments_count, 
                street_width = street_width, 
                # rooms = rooms , 
                # lounges = lounges, 
                # bathroom = bathrooms, 
                floor =floor, 
                property_age = property_age, 
                # family_part = family_part, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                # furnished = features[4], 
                # kitchen = features[5], 
                # extenstion = features[6], 
                # car_entrance = features[7], 
                # elevator = features[8], 
                # ac = features[9], 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2], 
                lat = lat, 
                lng = lng  
                # private_enternace = features[13], 
        )

        elif property_type == 'villa_rent': 
            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            families = request.POST.get('families') 
            furnished = request.POST.get('furnished') 
            kitchen = request.POST.get('kitchen') 
            extenstion = request.POST.get('extenstion') 
            car_entrance = request.POST.get('car_entrance') 
            elevator = request.POST.get('elevator') 
            ac = request.POST.get('ac') 
            pool = request.POST.get('pool')
            private_surface = request.POST.get('private_surface') 
            in_villa = request.POST.get('in_villa') 
            two_enternace = request.POST.get('two_enternace') 
            private_enternace = request.POST.get('private_enternace') 
            driver_room = request.POST.get("driver_room")
            maid_room = request.POST.get('maid_room')
            duplex = request.POST.get('duplex')
            basement = request.POST.get('basement')
            
            yard = request.POST.get('yard') 
            hair_tent_house = request.POST.get('hair_tent_house')

            features.append(families) # 3
            features.append(furnished) # 4
            features.append(kitchen) # 5
            features.append(extenstion) # 6 
            features.append(car_entrance) # 7
            features.append(elevator) # 8
            features.append(ac) # 9 
            features.append(private_surface) # 10 
            features.append(in_villa) # 11
            features.append(two_enternace) # 12
            features.append(private_enternace) # 13 
            features.append(driver_room) # 14
            features.append(maid_room) # 15
            features.append(duplex) # 16
            features.append(basement) # 17
            features.append(yard) # 18
            features.append(hair_tent_house) # 19 


            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create(
                user = user, 
                driver_room = features[14], 
                maid_room = features[15],
                duplex = features[16], 
                basement = features[17], 
                yard = features[18], 
                hair_tent_house = features[19],
                families = features[3], 
                private_surface = features[10], 
                in_villa = features[11], 
                two_enternace = features[12], 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                # interface= interface, 
                street_width = street_width, 
                rooms = rooms , 
                lounges = lounges, 
                bathroom = bathrooms, 
                floor =floor, 
                property_age = property_age, 
                # family_part = family_part, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                furnished = features[4], 
                kitchen = features[5], 
                extenstion = features[6], 
                car_entrance = features[7], 
                elevator = features[8], 
                ac = features[9], 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2], 
                private_enternace = features[13], 
            )

        elif property_type == 'resthouse_rent': 
            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            pool = request.POST.get('pool')
            football_field = request.POST.get('football_field') 
            volly_field = request.POST.get('volly_field') 
            hair_tent_house = request.POST.get('hair_tent_house')
            amusement = request.POST.get('amusement') 
            family_part = request.POST.get('family_part') 
            kitchen = request.POST.get('kitchen') 


            features.append(pool) # 3
            features.append(football_field) # 4
            features.append(volly_field) # 5
            features.append(hair_tent_house) # 6
            features.append(amusement) # 7
            features.append(family_part) # 8
            features.append(kitchen) # 9

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 
        
            property_obj = Property.objects.create( 
                user = user, 
                lat = lat, 
                lng = lng  , 
                amusement = features[7], 
                football_field = features[4], 
                volly_field = features[5], 
                hair_tent_house = features[6],
                pool = features[3], 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                # interface= interface, 
                street_width = street_width, 
                rooms = rooms , 
                lounges = lounges, 
                bathroom = bathrooms, 
                floor =floor, 
                property_age = property_age, 
                family_part = features[8], 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 

                kitchen = features[9], 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
            )

        elif property_type == 'commercial_office_rent': 
            
            interface = request.POST.get('interface-input') 

            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            furnished = request.POST.get('furnished') 

            features.append(furnished) 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user , 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                interface= interface, 
                street_width = street_width, 
                rooms = rooms , 
                lounges = lounges, 
                bathroom = bathrooms, 
                floor =floor, 
                property_age = property_age, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                furnished = features[3] 
            )




        elif property_type == 'land_rent': 
            purpose = request.POST.get('purpose-input')
            interface = request.POST.get('interface-input') 
            length = request.POST.get('length-input') 
            width = request.POST.get('width-input') 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user, 
                length = length, 
                width = width, 
                purpose = purpose, 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                # interface= interface, 
                street_width = street_width, 
                # property_age = property_age, 
                # family_part = features[8], 
                rent_type = rent_type, 
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
            )

        
        elif property_type =='building_rent': 
            interface = request.POST.get('interface-input') 
            purpose = request.POST.get('purpose-input')
            furnished = request.POST.get('furnished') 
            basement = request.POST.get('basement')
            stores_count = request.POST.get('stores-count-input')

            apartments_count = request.POST.get('extra-apartments-count-input') 
            if apartments_count == None or apartments_count == "" or apartments_count == 0: 
                apartments_count = request.POST.get("apartments-count-input")  
            

            features.append(furnished) # 3 
            features.append(basement)  # 4 


            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                interface= interface, 
                street_width = street_width, 
                property_age = property_age, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                furnished = features[3], 
                basement = features[4], 
                stores_count = stores_count, 
                apartments_count = apartments_count

            )


        elif property_type == 'branch_rent': 
            interface = request.POST.get('interface-input')
            
            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                interface= interface, 
                street_width = street_width, 
                property_age = property_age, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
            )


        elif property_type =='furnished_apartment_rent': 
            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            families = request.POST.get('families') 
            extenstion = request.POST.get('extenstion') 
            car_entrance = request.POST.get('car_entrance') 
            ac = request.POST.get('ac') 

            features.append(families)  # 3 
            features.append(extenstion) # 4 
            features.append(car_entrance) # 5
            features.append(ac)  # 6

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                street_width = street_width, 
                property_age = property_age, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                families = features[3], 
                extenstion = features[4], 
                car_entrance= features[5], 
                ac = features[6], 

            )
            


        elif property_type =='chalet_rent': 
            football_field = request.POST.get('football_field') # 3
            volly_field = request.POST.get('volly_field') # 4 
            hair_tent_house = request.POST.get('hair_tent_house') # 5
            amusement = request.POST.get('amusement') # 6
            family_part = request.POST.get('family_part') # 7
            kitchen = request.POST.get('kitchen') # 8 


            features.append(football_field)
            features.append(volly_field)
            features.append(hair_tent_house)
            features.append(amusement)
            features.append(family_part)
            features.append(kitchen)

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = property_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                street_width = street_width, 
                property_age = property_age, 
                rent_type = rent_type ,
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                football_field = features[3], 
                volly_field = features[4], 
                hair_tent_house = features[5], 
                amusement = features[6], 
                family_part = features[7], 
                kitchen = features[8], 
            )


        # upload images 
        
        for i in range(len(images)): 
            PropertyImage.objects.create(
                property = property_obj, 
                img = images[i] , 
                main = images_status[i]
            ).save() 


        
        ## redirect to sucessfully uploaded ad 
        return redirect(reverse('property:ad-uploaded'))




        

        
        
    print(property_type) 
    context = {
        'property_type': property_type
    }
    return render(request, 'property/add-property.html', context) 


def ad_uploaded(request): 
    context = {} 
    return render(request, 'pages/ad-uploaded-successfully.html', context)


@login_required(login_url='/auth/')
def add_to_favourite(request, property_number): 
    user = request.user 
    property = Property.objects.get(number = property_number)  

    Favourite.objects.create(property=property, user=user).save() 


    return redirect(reverse('property:property-details', kwargs={'number': property.number}))
    

    ## return to previous page 