from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from .models import * 
# from accounts.models import Favourite
import uuid 
import os 
import io 
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from django.core.files.base import ContentFile

# Create your views here.


@login_required
def add_property_interface(request):
    if request.user.is_superuser == False: 
        return redirect('/')
    user = request.user 
    if user.phone_number_verify_status == False: 
        return redirect('user:verify-phone-number') 
    context = {} 
    return render(request, 'property/add-property-interface.html', context)


def property_details(request, number): 
    property = Property.objects.get(number = number)
    if property.draft == True: 
        return redirect('page:index')
    property.visits+=1 
    property.save() 
    if request.user.is_authenticated: 

        is_favourite = False 
        try: 
            ad = Favourite.objects.get(user=request.user, ad=property) 
            is_favourite = True
        except Favourite.DoesNotExist: 
            is_favourite = False 

        context = {
            'property': property, 
            'is_favourite': is_favourite
        } 
    else: 
        context = {
            'property': property, 
        } 
    return render(request, 'property/property-details.html', context ) 


def add_watermark(image, logo_path, position=(0, 0)):
    opacity= .5
    # Open the original image and the logo
    base_image = Image.open(image)
    watermark = Image.open(logo_path).convert("RGBA")

    # Resize the watermark to fit the base image (optional)
    width, height = base_image.size
    watermark.thumbnail((width // 4, height // 4), Image.ANTIALIAS)

    if opacity < 1:
        # Split the watermark into its RGB and Alpha channels
        r, g, b, alpha = watermark.split()
        
        # Enhance the alpha channel to reduce opacity
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        
        # Recombine the channels
        watermark = Image.merge('RGBA', (r, g, b, alpha))

    # Calculate the position to paste the watermark
    watermark_width, watermark_height = watermark.size
    if position == 'center':
        position = ((width - watermark_width) // 2, (height - watermark_height) // 2)
    elif position == 'bottom_right':
        position = (width - watermark_width - 10, height - watermark_height - 10)

    # Paste the watermark on the original image
    base_image.paste(watermark, position, watermark)

    # Save the watermarked image in memory
    output = io.BytesIO()
    base_image.save(output, format='JPEG')
    return ContentFile(output.getvalue())

@login_required(login_url='/auth/')
def add_property(request, property_type, offer_type=None): 
    if request.user.is_superuser == False: 
        return redirect('/')
    user = request.user 
    if user.phone_number_verify_status == False: 
        return redirect('user:verify-phone-number') 

    if offer_type == "sell":
        sell = 1 
        if property_type == "commercial_office_rent": 
            p_type = "commercial_office_sale"
        else: 
            p_type = str(property_type).split("_")[0]+"_sale"
        print(p_type) 
    else: 
        sell = 0 
        p_type = property_type



    # property_type_display_name = PropertyDepartment.objects.get(name=p_type) 
    
    if request.POST: 


        license_num = request.POST.get('license_num') 
        fal_number = request.POST.get('fal_number') 


        ## payment types 
        monthly_payment = request.POST.get('monthly_payment') 
        quarterly_payment = request.POST.get('quarterly_payment') 
        semi_annual_payment = request.POST.get('semi_annual_payment') 
        annual_payment = request.POST.get('annual_payment')

        payments= [

        ]

        payments.append(monthly_payment) # 0
        payments.append(quarterly_payment) # 1 
        payments.append(semi_annual_payment) # 2 
        payments.append(annual_payment) # 4 

        for i in range(len(payments)) : 
            if payments[i] == 'on': 
                payments[i] = 1 
            else: 
                payments[i] = 0 

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
        new_filename = None 
        
        if video != None: 

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

            # families_or_single = request.POST.get('families_or_single') 


            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            interface = request.POST.get('interface-input') 


            families = request.POST.get('families') 
            single = request.POST.get('single') 
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
            features.append(single) # 14 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create(
                license_num = license_num, 
                fal_number = fal_number, 
                sale = sell, 
                interface = interface, 
                user= user, 
                p_type = p_type, 
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
                single = features[14], 
                families = features[3], 
                lat = lat, 
                lng = lng ,
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
                # families_or_single = families_or_single
        )

        
        elif property_type == 'shop_rent' or property_type == 'shop_sale': 
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
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                p_type = p_type, 
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
                property_age = p_type, 
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

        elif property_type == 'villa_rent' or property_type == 'villa_sale': 
            interface = request.POST.get('interface-input') 
            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            families = request.POST.get('families') 
            single = request.POST.get('single') 
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
            features.append(single) # 20 


            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create(
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                lat= lat, 
                lng=lng,
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
                p_type = p_type, 
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
                single = features[20], 
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )

        elif property_type == 'resthouse_rent' or property_type == 'resthouse_sale': 
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
            single = request.POST.get('single') 



            features.append(pool) # 3
            features.append(football_field) # 4
            features.append(volly_field) # 5
            features.append(hair_tent_house) # 6
            features.append(amusement) # 7
            features.append(family_part) # 8
            features.append(kitchen) # 9
            features.append(single) # 10 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 
        
            property_obj = Property.objects.create( 
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                amusement = features[7], 
                football_field = features[4], 
                volly_field = features[5], 
                hair_tent_house = features[6],
                pool = features[3], 
                p_type = p_type, 
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
                single = features[10], 
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )

        elif property_type == 'commercial_office_rent' or property_type == 'commercial_office_sale': 
            
            
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
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user , 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
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
                furnished = features[3] , 
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )



        elif property_type == 'land_rent' or property_type == 'land_sale': 
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
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                length = length, 
                width = width, 
                purpose = purpose, 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                interface= interface, 
                street_width = street_width, 
                # property_age = property_age, 
                # family_part = features[8], 
                rent_type = rent_type, 
                # purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3],  
            )

        
        elif property_type =='building_rent' or property_type == 'building_sale': 
            interface = request.POST.get('interface-input') 
            purpose = request.POST.get('purpose-input')
            furnished = request.POST.get('furnished') 
            basement = request.POST.get('basement')
            stores_count = request.POST.get('stores-count-input')
            single = request.POST.get('single') 
            families = request.POST.get('families') 



            apartments_count = request.POST.get('extra-apartments-count-input') 
            if apartments_count == None or apartments_count == "" or apartments_count == 0: 
                apartments_count = request.POST.get("apartments-count-input")  
            

            features.append(furnished) # 3 
            features.append(basement)  # 4 
            features.append(single) # 5 
            features.append(families) # 6 



            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type =p_type, 
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
                purpose = purpose, 
                description = description, 
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                furnished = features[3], 
                basement = features[4], 
                stores_count = stores_count, 
                apartments_count = apartments_count, 
                single = features[5], 
                families = features[6], 
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )


        elif property_type == 'branch_rent' or property_type == 'branch_sale': 
            interface = request.POST.get('interface-input')
            
            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
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
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )


        elif property_type =='furnished_apartment_rent': 
            single = request.POST.get('single') 

            floor = request.POST.get('extra-floor-input') 
            if floor == None or floor == '' or floor == 0: 
                floor = request.POST.get('floor-input') 

            # families_or_single = request.POST.get('families_or_single') 

            lounges = request.POST.get('extra-lounges-input') 
            if lounges == None or lounges == "" or lounges == 0: 
                lounges = request.POST.get('lounges-input') 
            

            families = request.POST.get('families') 
            extenstion = request.POST.get('extenstion') 
            car_entrance = request.POST.get('car_entrance') 
            ac = request.POST.get('ac') 

            features.append(families)  # 3 
            features.append(extenstion) # 4 
            features.append(car_entrance) # 5
            features.append(ac)  # 6
            features.append(single) # 7 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                lounges= lounges, 
                floor= floor, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
                neighborhood = neighborhood, 
                city = city, 
                rooms=rooms, 
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
                single = features[7],
                # families_or_single = families_or_single
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )
            
        elif property_type == 'farm_sale': 
            interface = request.POST.get('interface-input') 
            trees_count = request.POST.get('trees-count-input') 
            wells_count = request.POST.get('wells-count-input') 
            hair_tent_house = request.POST.get('hair_tent_house')  

            features.append(hair_tent_house) 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                license_num = license_num, 
                fal_number = fal_number,
                interface = interface, 
                trees = trees_count, 
                wells = wells_count, 
                
                sale = sell, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
                neighborhood = neighborhood, 
                city = city, 
                price = price, 
                space = space, 
                advertiser_relation= advertiser_relation, 
                exclusive = exclusive, 
                video = video, 
                street_width = street_width, 
                property_age = property_age, 
                
                water_exist = features[0], 
                power_exist = features[1], 
                sanitation_exist = features[2],  
                hair_tent_house = features[3], 

            )            


        elif property_type =='chalet_rent' or property_type == 'chalet_sale': 

            football_field = request.POST.get('football_field') # 3
            volly_field = request.POST.get('volly_field') # 4 
            hair_tent_house = request.POST.get('hair_tent_house') # 5
            amusement = request.POST.get('amusement') # 6
            family_part = request.POST.get('family_part') # 7
            kitchen = request.POST.get('kitchen') # 8 
            furnished = request.POST.get('furnished') # 9
            single = request.POST.get('single')  # 10 
            pool = request.POST.get('pool') # 11 
            interface = request.POST.get('interface-input') 

            features.append(football_field)
            features.append(volly_field)
            features.append(hair_tent_house)
            features.append(amusement)
            features.append(family_part)
            features.append(kitchen)
            features.append(furnished)
            features.append(single) 
            features.append(pool) 

            for i in range(len(features)) : 
                if features[i] == 'on': 
                    features[i] = 1 
                else: 
                    features[i] = 0 

            property_obj = Property.objects.create( 
                interface = interface, 
                license_num = license_num, 
                fal_number = fal_number,
                sale = sell, 
                user = user, 
                lat = lat, 
                lng = lng  , 
                p_type = p_type, 
                bathroom = bathrooms, 
                neighborhood = neighborhood, 
                lounges = lounges, 
                rooms = rooms, 
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
                furnished = features[9], 
                single= features[10], 
                pool = features[11],
                monthly_payment= payments[0] ,
                quarterly_payment = payments[1], 
                semi_annual_payment = payments[2], 
                annual_payment = payments[3], 
            )


        # upload images 
        # logo_path = "logo.jpeg" 
        logo_path =  Watermark.objects.last().img.path 

        """
        for i in range(len(images)): 
            watermarked_image = add_watermark(images[i], logo_path, position='bottom_right')


            PropertyImage.objects.create(
                property = property_obj, 
                # img = images[i] , 
                img = watermarked_image, 
                main = images_status[i]
            ).save() 

        """


        for i in range(len(images)):
            # Add watermark to the image
            # watermarked_image = add_watermark(images[i], logo_path, position='center')
            watermarked_image = images[i]

            # Create the PropertyImage object
            property_image = PropertyImage(
                property=property_obj,
                main=images_status[i]
            )

            # Assign the watermarked image to the img field
            property_image.img.save(f"{images[i].name}", watermarked_image, save=False)
            
            # Save the model instance to the database
            property_image.save()
        
        ## redirect to sucessfully uploaded ad 
        return redirect(reverse('property:ad-uploaded'))

 
    context = {
        'property_type': property_type, 
        'offer_type': offer_type,
        # 'property_type_display_name': property_type_display_name, 
    }
    return render(request, 'property/add-property.html', context) 


def ad_uploaded(request): 
    context = {} 
    return render(request, 'pages/ad-uploaded-successfully.html', context)


@login_required
def add_to_favourite(request, property_number): 
    user = request.user 

    property = Property.objects.get(number = property_number)  

    try: 
        ad = Favourite.objects.get(user=user, ad=property)
        ad.delete() 
        is_favourite = False 

    except Favourite.DoesNotExist: 
        ad = Favourite.objects.create(ad=property, user=user) 
        is_favourite = True 


    return redirect(reverse('property:property-details', kwargs={'number': property.number}))
    

    ## return to previous page 



def report_property(request, number): 
    property = Property.objects.get(number=number) 
    Report.objects.create(ad=property, number=number) 

    context = {} 

    return redirect(reverse("property:reported"))



def show_reported(request): 
    context = {} 
    return render(request, 'property/reported.html', context=context )    




def filter_properties(request):
    # property_type = request.GET.get('p_type')
    filters = request.GET.dict()
    p_type = filters['p_type']


    # Remove 'property_type' from filters
    del filters["p_type"]

    new_filters = {'p_type': p_type}

    for i in filters.items(): 
        if i[1] != '': 
            new_filters[i[0]] = i[1]
    
    print(new_filters)

    # Construct filter query
    filter_query = { 'p_type': p_type }
    for key, value in filters.items():
        filter_query[key] = value

    # Filter properties
    filtered_properties = Property.objects.filter(**new_filters)

    print(type(filter_properties))
    print('*'* 30) 

    context = {
        'result': list(filtered_properties)
    }


    # return JsonResponse(list(filtered_properties), safe=False)
    return render(request, 'property/filter-results.html', context)



def filter_result(request, p_type):
    if p_type != 'all': 
        p_type_parent  = str(p_type).split('_')[0]
        print(p_type_parent)
        properties = Property.objects.filter(draft=False).filter(p_type__icontains=p_type_parent)[::-1]
    else: 
        properties = Property.objects.all()[::-1]

    context = {
        'result': properties
    }

    return render(request, 'property/filter-results.html', context)