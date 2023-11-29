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
        center: { lat: Number(latInput.value), lng: Number(lngInput.value) }, // Coordinates for Saudi Arabia
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
        position: {lat: Number(latInput.value), lng: Number(lngInput.value)},
    });




    

}



window.initMap = initMap;
// initMap(); 



