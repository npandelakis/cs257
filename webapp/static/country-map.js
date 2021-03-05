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
        },
        done: function(datamap){
            datamap.svg.call(d3.behavior.zoom().on("zoom", redraw));
            function redraw() {

                datamap.svg.selectAll(".datamaps-marker")
                .attr("height", 20/d3.event.scale)
                .attr("width", 20/d3.event.scale)
                .attr("x", function(markerData) {
                    return markerData.realx - 20/d3.event.scale/2;
                })
                .attr("y", function(markerData) {
                    return markerData.realy - 20/d3.event.scale;
                });
                datamap.svg.selectAll("g").attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");

            }
        }
    });



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
          if (latLng) {
            markerData.realx = latLng[0];
            return (latLng[0] - (options.icon.width / 2));
          }
        })
        .attr('y', function (markerData) {
          var latLng;
          if (markerHasCoordinates(markerData)) {
            latLng = self.latLngToXY(markerData.latitude, markerData.longitude);
          }
          else if (markerData.centered) {
            latLng = self.path.centroid(svg.select('path.' + markerData.centered).data()[0]);
          }
          if (latLng){
              markerData.realy = latLng[1];
              return (latLng[1] - options.icon.height);
          }
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
            if (data.summary) {
                summary = data.summary;
                var template = '<div class = "hoverpopup">'+ summary + '</div>';
                return template;
            } else {
                var template = '<div class = "hoverpopup">No Summary Available.</div>';
                return template;
            }
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

        if (attack.latitude !== "None" && attack.longitude !== "None") {

            mapMarkers.push({
                "name" : attack.id,
                "radius" : 10,
                "latitude": attack.latitude,
                "longitude": attack.longitude,
                "summary" : attack.summary
            });
        }
    };

    return mapMarkers;

}

function getCountryCode() {
    var pathname = window.location.pathname;
    return pathname.split('/').pop();
}

async function getCentroid(countryCode) {
    var url = 'http://localhost:5000/api/centroid/' + countryCode;
    var data = await fetch(url).then((response) => response.json()).then(data => {return data;});


    return [data[0].longitude, data[0].latitude];
}
