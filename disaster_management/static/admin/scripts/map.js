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

// Fetch data from the server
fetch('/admin/send_loc')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Process the data here
    console.log(data);
    // Example: Assuming data is an array of objects with pincode and danger properties
    data.forEach(location => {
      var pincode = location.Pincode;
      var isDangerous = location.danger;
      addDisasterLocation(pincode, isDangerous);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

map.zoomControl.setPosition('bottomright');
