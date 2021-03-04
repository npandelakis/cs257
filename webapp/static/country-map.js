/* world-map.js
 *
 * Javascript to query the /api/country/<country_code> endpoint
 * and display the data on a world map.
 *
 * Written by Nick Pandelakis and Grace de Benedetti
 */

window.onload = initialize;

function initialize() {
    initializeMap();
}


async function initializeMap() {
    var countryCode = getCountryCode();

    const centroid = await getCentroid(countryCode);

    var element = document.getElementById('map-container');



    var map = new Datamap({
        element: element,
        scope: countryCode,
        data: {},
        setProjection: function(element) {
            var projection = d3.geo.equirectangular()
                .center(centroid)
                .translate([element.offsetWidth / 2, element.offsetHeight / 2])
                .scale(Math.min(element.offsetWidth,element.offsetHeight))
            var path = d3.geo.path()
                .projection(projection);

            return {
                path: path,
                projection: projection
            };
        },
        geographyConfig: {
            highlightOnHover: false,
            popupOnHover: false
        }
    });

    //console.log(d3.select("g").append("svg").attr("width", element.offsetWidth).attr("height", element.offsetHeight));
    var svg = d3.select("g").append("svg").attr("width", element.offsetWidth).attr("height", element.offsetHeight).append("g");


    //Only way I could get this to work was to copy paste it in from another file.
    //Credit to arshad https://github.com/arshad/datamaps-custom-marker
    map.addPlugin('markers', function (layer, data, options) {
      var self = this,
        fillData = this.options.fills,
        svg = this.svg;

      // Check for map data.
      if (!data || (data && !data.slice)) {
        throw "Datamaps Error - markers must be an array";
      }

      // Build markers.
      var markers = layer
        .selectAll('image.datamaps-markers')
        .data(data, JSON.stringify);

      markers
        .enter()
        .append('image')
        .attr('class', 'datamaps-marker')
        .attr('xlink:href', options.icon.url)
        .attr('width', options.icon.width)
        .attr('height', options.icon.height)
        .attr('x', function (markerData) {
          var latLng;
          if (markerHasCoordinates(markerData)) {
            latLng = self.latLngToXY(markerData.latitude, markerData.longitude);
          }
          else if (markerData.centered) {
            latLng = self.path.centroid(svg.select('path.' + markerData.centered).data()[0]);
          }
          if (latLng) return (latLng[0] - (options.icon.width / 2));
        })
        .attr('y', function (markerData) {
          var latLng;
          if (markerHasCoordinates(markerData)) {
            latLng = self.latLngToXY(markerData.latitude, markerData.longitude);
          }
          else if (markerData.centered) {
            latLng = self.path.centroid(svg.select('path.' + markerData.centered).data()[0]);
          }
          if (latLng) return (latLng[1] - options.icon.height);
        })
        .on('mouseover', function (markerData) {
          var $this = d3.select(this);
          if (options.popupOnHover) {
            self.updatePopup($this, markerData, options, svg);
          }
        })
        .on('mouseout', function (markerData) {
          var $this = d3.select(this);
          if (options.highlightOnHover) {
            // Reapply previous attributes.
            var previousAttributes = JSON.parse($this.attr('data-previousAttributes'));
            for (var attr in previousAttributes) {
              $this.style(attr, previousAttributes[attr]);
            }
          }
          d3.selectAll('.datamaps-hoverover').style('display', 'none');
        })

      markers.exit()
        .transition()
        .delay(options.exitDelay)
        .attr("height", 0)
        .remove();

      // Checks if a marker has latitude and longitude provided.
      function markerHasCoordinates(markerData) {
        return typeof markerData !== 'undefined' && typeof markerData.latitude !== 'undefined' && typeof markerData.longitude !== 'undefined';
      }
  });

    var options = {
        fillOpacity: 1,
        highlightOnHover: true,
        popupOnHover: true,
        popupTemplate: function(data) {
            var summary = '';
            if (data && 'summary' in data) {
                summary = data.summary;
            }
            var template = '<div class = "hoverpopup">'+ summary + '</div>';
            return template;
        },
        icon: {
            url: '/static/map-marker.png',
            width: 20,
            height: 20
        }
    };

    const markers = await getMapMarkers();

    map.markers(markers, options);
}


async function getMapMarkers() {
    var start_year = document.getElementById('start_year');
    var end_year = document.getElementById('end_year');
    var country_code = getCountryCode();

    var url = 'http://localhost:5000/api/countries/' + country_code;

    var data = await fetch(url).then((response) => response.json()).then(data => {return data;});

    var mapMarkers = [];

    for (var i = 0; i < data.length; i++) {

        var attack = data[i];

        mapMarkers.push({
            "name" : attack.id,
            "radius" : 10,
            "latitude": attack.latitude,
            "longitude": attack.longitude,
            "summary" : attack.summary
        });
    };

    return mapMarkers;

}

function getCountryCode() {
    var pathname = window.location.pathname;
    console.log(pathname)
    return pathname.split('/').pop();
}

async function getCentroid(countryCode) {
    var url = 'http://localhost:5000/api/centroid/' + countryCode;
    var data = await fetch(url).then((response) => response.json()).then(data => {return data;});


    return [data[0].longitude, data[0].latitude];
}
