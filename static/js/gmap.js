var myCenter = new google.maps.LatLng(51.5073509,-0.12775829999998223);

function initialize() {
    var mapProp = {
        center: myCenter,
        scrollwheel: false,
        zoom:15,
        zoomControl: false,
        mapTypeControl: false,
        streetViewControl: false,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: [{ "featureType": "landscape", "stylers": [{ "color": "#e8e4d9" }, { "visibility": "on" }] }, { "featureType": "poi", "stylers": [{ "saturation": -100 }, { "lightness": 51 }, { "visibility": "simplified" }] }, { "featureType": "road.highway", "stylers": [{ "color": "#ffe161" }, { "visibility": "on" }] }, { "featureType": "road.arterial", "stylers": [{ "color": "#ffe361" }, { "visibility": "on" }] }, { "featureType": "road.local", "stylers": [{ "color": "#ffe361" }, { "visibility": "off" }] }, { "featureType": "transit", "stylers": [{ "saturation": -100 }, { "visibility": "simplified" }] }, { "featureType": "administrative.province", "stylers": [{ "visibility": "off" }] }, { "featureType": "water", "elementType": "labels", "stylers": [{ "visibility": "on" }, { "color": "#b0cffe" }] }, { "featureType": "water", "elementType": "geometry", "stylers": [{ "color": "#e9e5dc" }, { "visibility": "on" }] }]
    };

    var map = new google.maps.Map(document.getElementById("gmap"), mapProp);
        

    var marker = new google.maps.Marker({
        position: myCenter,
    });

    marker.setMap(map);


}

google.maps.event.addDomListener(window, 'load', initialize);