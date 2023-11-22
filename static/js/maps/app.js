const cities = [
    ["Riyadh", 24.7136, 46.6753],
    ["Jeddah", 21.4858, 39.2192],
    ["Mecca", 21.3891, 39.8262],
    ["Medina", 24.5247, 39.8382],
    ["Dammam", 26.3927, 50.1474],
    ["Khobar", 26.2975, 50.2044],
    ["Dhahran", 26.2947, 50.1516],
    ["Abha", 18.2340, 42.5053],
    ["Taif", 21.2703, 40.4167],
    ["Buraidah", 26.3260, 43.9750],
    ["Tabuk", 28.3835, 36.5860],
    ["Hail", 27.5208, 41.6916],
    ["Najran", 17.5274, 44.1300],
    ["Jubail", 27.0112, 49.5800],
    ["Yanbu", 24.0915, 38.0637],
    ["Al Hofuf", 25.3645, 49.5874],
    ["Khamis Mushait", 18.3060, 42.7960],
    ["Al-Qatif", 26.5334, 50.0075],
    ["Al Khafji", 28.4344, 49.9711],
    ["Al Bahah", 20.0123, 41.7686],
    ["Sakakah", 29.9717, 40.2075],
    ["Arar", 30.9753, 41.0341],
    ["Jizan", 16.8870, 42.5792],
    ["Rabigh", 22.7987, 39.0419],
    ["Al Baha", 20.0059, 41.6327],
    ["Al-Mubarraz", 25.4195, 49.6300],
    ["Al Wajh", 26.2323, 36.4656],
    ["Hafr Al-Batin", 28.4434, 46.6750]
];




let infoCard = document.querySelector('.info-card'); 
let infoCardP = infoCard.querySelector('p');
let infoCardH3 = infoCard.querySelector('h3'); 
let infoCardCloseBtn = infoCard.querySelector('#close-btn'); 
let mapOptions = document.querySelector('.map-options'); 


infoCardCloseBtn.addEventListener('click', () => {
    infoCard.style.display = 'none';
    mapOptions.style.display ='flex';
})

async function initMap() {

    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new google.maps.Map(document.getElementById("map"), {
        mapId: "6a7f4f4e7a7f5b47",
        center: { lat: 23.885942, lng: 45.079163 }, // Coordinates for Saudi Arabia
        zoom: 6, 
        zoomControl: false, 
        // mapTypeControl: true,
        mapTypeControlOptions: {
            mapTypeIds: ['roadmap', 'terrain', 'satellite']
        },
        mapTypeId: "terrain",
        fullscreenControl: false, 
        gestureHandling: "greedy"  
    });


    const priceTag = document.createElement("div");

    priceTag.className = "price-tag";
    priceTag.textContent = "1030"
  
    // const AdvMarker = new AdvancedMarkerElement ({
    //     position: { lat: 24.7136, lng: 46.6753 }, 
    //     map: map, 
    //     content: priceTag 
    // })



    cities.forEach((city) => {

        const priceTag = document.createElement("div");

        priceTag.className = "price-tag";
        priceTag.textContent = "10 مليون"
        
        const marker = new AdvancedMarkerElement ({
            map,
            position: { lat: city[1], lng: city[2] },
            content: priceTag, 
            // icon: './house(1).png',
        });


    
        marker.addListener('click', function () {
            // alert(city[0]) 
            infoCard.style.display = 'block'; 
            infoCardH3.textContent = city[0]; 

            mapOptions.style.display = 'none'; 
            
        });



    })


    document.querySelector("#btn_satellite").addEventListener('click', function() {
        map.setMapTypeId('satellite')
    })


    document.querySelector("#btn_roadmap").addEventListener('click', function() {
        map.setMapTypeId('roadmap')
    })

    document.querySelector("#btn_terrain").addEventListener('click', function() {
        map.setMapTypeId('terrain')
    })


}



window.initMap = initMap;
// initMap(); 



