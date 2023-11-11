let latInput = document.querySelector('#lat-input'); 
let lngInput = document.querySelector('#lng-input'); 

function reverseGeocode(lat, lng) {
    var geocoder = new google.maps.Geocoder();
    var latLng = new google.maps.LatLng(lat, lng);

    geocoder.geocode({ 'location': latLng }, function (results, status) {
        if (status === 'OK') {
            if (results[0]) {

                
                var addressComponents = results[0].address_components;

                console.log(addressComponents); 

                var neighborhood, city;

                let neighborhoodInput = document.querySelector('[name=neighborhood-input]')
                let cityInput = document.querySelector('[name=city-input]'); 

                
                for (var i = 0; i < results[0].address_components.length; i++) {
                    var component = results[0].address_components[i];
                    if (component.types.includes('neighborhood') || component.types.includes('sublocality')) {
                      neighborhood = component.long_name;
                    } else if (component.types.includes('locality')) {
                      city = component.long_name;
                    }
                }

                neighborhoodInput.value = neighborhood; 
                cityInput.value = city; 

                // console.log(neighborhoodInput) ; 
                // console.log(cityInput); 
                

        //         for (var i = 0; i < addressComponents.length; i++) {
        //             var component = addressComponents[i];
        //             if (component.types.includes('neighborhood')) {
        //                 neighborhood = component.long_name;
        //             }
        //             if (component.types.includes('locality')) {
        //                 city = component.long_name;
        //             }
        //         }

        //         if (neighborhood && city) {
        //             console.log("Neighborhood: " + neighborhood);
        //             console.log("City: " + city);
        //         } else {
        //             console.log("Neighborhood or City not found.");
        //         }
        //     } else {
        //         console.log("No results found");
        //     }
        // } else {
        //     console.log("Geocoder failed due to: " + status);
        }}
    });
}



async function initMap() {

    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new google.maps.Map(document.getElementById("map"), {
        mapId: "6a7f4f4e7a7f5b47",
        center: { lat: 26.403121781303653, lng: 43.917549974016744 }, // Coordinates for Saudi Arabia
        zoom: 24, 
        zoomControl: false, 
        mapTypeId: "roadmap",
        mapTypeControl: false, 
        fullscreenControl: false, 
        gestureHandling: "greedy", 
        streetViewControl: false, 
    });

    var userMarker = new google.maps.Marker({
        map: map,
        draggable: false, 
        animation: google.maps.Animation.DROP, 
        position: map.getCenter(),
    });

    google.maps.event.addListener(map, 'drag', function() {
        // Update the marker position to the center of the map
        userMarker.setPosition(map.getCenter());
        const position = userMarker.position 
        const lat = position.lat(); // دوائر العرض
        const lng = position.lng(); // خطوط الطول
        latInput.value = lat ;
        lngInput.value = lng; 
        reverseGeocode(lat, lng) 
    });


    google.maps.event.addListener(map, 'zoom_changed', function () {
        userMarker.setPosition(map.getCenter());
        const position = userMarker.position 
        const lat = position.lat(); // دوائر العرض
        const lng = position.lng(); // خطوط الطول
        latInput.value = lat ;
        lngInput.value = lng; 
        reverseGeocode(lat, lng) 
    });



    // userMarker.addListener('dragend', function () {
    //     const position = userMarker.position 
    //     const lat = position.lat(); // دوائر العرض
    //     const lng = position.lng(); // خطوط الطول
    //     latInput.value = lat ;
    //     lngInput.value = lng; 

    //     console.log(lat) ;
    //     console.log(lng) ; 
        
    //     reverseGeocode(lat, lng) 
    // })


    

    let myLocationButton = document.getElementById('myLocationButton')

    myLocationButton.addEventListener('click', function() {
        // Check if geolocation is available in the user's browser
        if (navigator.geolocation) {
            // Get the user's current location
            navigator.geolocation.getCurrentPosition(function(position) {
                var userLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    
                // Set the map's center to the user's location
                map.setCenter(userLatLng);
    
                // Set the marker's position to the user's location
                userMarker.setPosition(userLatLng);
    
                // Optionally, you can open an info window or perform other actions here
            }, function(error) {
                // Handle any errors here, such as permission denied or unable to retrieve location
                console.error('Error getting user location:', error);
            });
        } else {
            // Geolocation is not supported in this browser
            alert('Geolocation is not supported in your browser.');
        }
    });


    let btnTerrain = document.querySelector(".btn-terrain")
    btnTerrain.addEventListener('click', () => {
        btnTerrain.classList.toggle('enabled')
        if (btnTerrain.classList.contains("enabled")) { 
            map.setMapTypeId(google.maps.MapTypeId.ROADMAP); 
        } else { 
            map.setMapTypeId(google.maps.MapTypeId.SATELLITE); 
        }
    })
  

}



window.initMap = initMap;
// initMap(); 



