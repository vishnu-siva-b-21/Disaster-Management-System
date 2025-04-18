// Set up initial map center and zoom level for South India, Tamil Nadu
var map = L.map('map').setView([15.1271, 76.6569], 5.5);

// Load basemap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to add a disaster location marker and danger zone circle
function addDisasterLocation(pincode, isDangerous) {
  // Perform geocoding to find latitude and longitude
  $.getJSON('https://nominatim.openstreetmap.org/search?format=json&q=' + pincode, function(data) {
    if (data.length > 0) {
      var latitude = parseFloat(data[0].lat);
      var longitude = parseFloat(data[0].lon);

      // Define circle color based on danger status
      var circleColor = isDangerous ? 'red' : 'orange';

      // Add danger zone circle with tooltip
      var circle = L.circle([latitude, longitude], {
        color: circleColor,
        fillColor: circleColor,
        fillOpacity: 0.5,
        radius: 50000 // Adjust radius as needed, in meters
      }).addTo(map);

      // Tooltip to show area name and pincode on hover
      circle.bindTooltip('<b>Area Name:</b> ' + data[0].display_name + '<br><b>Pincode:</b> ' + pincode);
    } else {
      console.log('Pincode not found:', pincode);
    }
  });
}

var data = [
  { pincode: '612105', danger: false },
  { pincode: '632009', danger: true },
  { pincode: '600099', danger: true }
];

// Iterate through static data
data.forEach(function(location) {
  var pincode = location.pincode;
  var isDangerous = location.danger;
  addDisasterLocation(pincode, isDangerous);
});

map.zoomControl.setPosition('bottomright');