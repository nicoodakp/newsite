function getWeatherData(lat, long){
     var apiKey = "693bfc720a2fc19b10c0d12926307eb7";
     var exclude = "?exclude=minutely,hourly,daily,alerts,flags";
     var unit = "?units=si";
     var url = "https://api.darksky.net/forecast/" + apiKey + "/" + lat + "," + long + exclude + unit;

    //get darksky api data
    $.ajax({
      url: url,
      dataType: "jsonp",
      success: function (weatherData) {
        //icon information (explained after)
        var icon = weatherData.currently.icon;
        //weather description
        var description = weatherData.currently.summary;
        //change background image
        //temperature
        var temperature = weatherData.currently.temperature;
      }
    });
  }

  $('#weather-description').text(weatherData.currently.summary);
  $('#weather-value').val(weatherData.currently.temperature);
