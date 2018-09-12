var url = "https://maps.googleapis.com/maps/api/geocode/json?latlng="+ lat + "," + long;
$.getJSON(url, function(data) {
   var arr_address_comp = data.results[2].formatted_address;
   arr_address_comp.forEach(function(val) {
      if(val.types[0] === "locality" ){
         cityName = val.long_name;
      }
      if(val.types[0] === "country" ){
         countryCode = val.short_name;
         countryName = val.long_name;
      }
   });
   //set your tag element where you will describethe location
   $('#weather-location').text(cityName + ", " + countryName);
});
