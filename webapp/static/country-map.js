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

            //Handle and scale the map for zooming
            datamap.svg.call(d3.behavior.zoom().on("zoom", redraw));
            function redraw() {

                datamap.svg.selectAll(".datamaps-marker")
                .attr("height", 20/d3.event.scale)
                .attr("width", 20/d3.event.scale)
                .attr("x", function(markerData) {
                    return markerData.realx - 20/d3.event.scale/2;
                })
                .attr("y", function(markerData) {
                    return markerData.realy - 20/d3.event.scale ;
                });

                datamap.svg.selectAll("g")
                .attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
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

    addMarkers(map);

    const filterButton = document.getElementById("filter-button");

    //cleanup and redraw map markers when filtering
	filterButton.addEventListener("click", async function() {
        map.svg.selectAll(".datamaps-marker").remove();
		addMarkers(map);
	})

}


async function addMarkers(map) {
    var options = {
        fillOpacity: 1,
        highlightOnHover: true,
        popupOnHover: true,
        popupTemplate: function(data) {
            var summary = '';
            if (data.summary) {
                summary = data.summary;
                var template = '<div class = "hoverpopup"><strong>Attack ' + data.id +'</strong> (Click to learn more!)<br>\n'
                + summary + '</div>';
                return template;
            } else {
                var template = '<div class = "hoverpopup"><strong>Attack ' + data.id +'</strong> (Click to learn more!) <br>\n'
                + data.date + '<br>\n'
                + 'No Summary Available.</div>';
                return template;
            }
        },
        icon: {
            url: '/static/map-marker.png',
            width: 20,
            height: 20
        }
    };

    var markers = await getMapMarkers();

    map.markers(markers, options);

    map.svg.selectAll(".datamaps-marker").on("click", onMarkerClick);
}

function onMarkerClick(data) {
    if (drag == false) {
        window.location = "/countries/" + getCountryCode() + "/" + data.id;
    }
}

async function getMapMarkers() {
    var start_year = document.getElementById('start_year');
    var end_year = document.getElementById('end_year');
    var country_code = getCountryCode();

    if (start_year.value && end_year.value) {
		var url = getBaseUrl() + 'api/countries/' + country_code + '?start_year=' + start_year.value
			  + '&end_year=' + end_year.value;
	} else {
		var url = getAPIBaseUrl() + 'api/world';
	}

    var data = await fetch(url).then((response) => response.json()).then(data => {return data;});


    var mapMarkers = [];

    for (var i = 0; i < data.length; i++) {
        var attack = data[i];

        if (attack.latitude !== "None" && attack.longitude !== "None") {

            mapMarkers.push({
                "id" : attack.id,
                "date" : attack.month + '/' + attack.day + '/' + attack.year,
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
    var url = getBaseUrl() + 'api/centroid/' + countryCode;
    var data = await fetch(url).then((response) => response.json()).then(data => {return data;});


    return [data[0].longitude, data[0].latitude];
}

function getBaseUrl() {
    return window.location.protocol + '//' + window.location.host + '/'
}

function getAPIBaseUrl() {
	var getUrl = window.location;
	var baseUrl = getUrl.protocol + '//' + getUrl.host + '/';
	return baseUrl;
}

//search
document.addEventListener("DOMContentLoaded", function() {
	const button = document.getElementById("search-button");
	const searchBar = document.getElementById("search_bar");

	button.addEventListener("click", () => {
		var value = searchBar.value;
		var value = value.slice(-3);
		var value = value.toLowerCase();
		window.location = 'countries/' + value;
	})


	async function getCountryOptions(callback){
		// Get the <datalist> and <input> elements.
		var input = document.getElementById("search_bar");
		var url = getAPIBaseUrl() + '/api/countrynames/' + input.value;
		const searchResponse = await fetch(url);
		return searchResponse.text();
	}

	searchBar.addEventListener("keyup", () =>{
        var dataList = document.getElementById("countries");
        dataList.innerHTML = '';
		if (searchBar.value == ''){}
		else{datalistOptions();
		}
	})
	async function datalistOptions(){
		//var datalist_options = JSON.parse(searchResponse);
		var dataList = document.getElementById("countries");
		var searchResponse = await getCountryOptions();
		var searchResponseArray = JSON.parse(searchResponse);
		searchResponseArray.forEach (function(item) {
	        // Create a new <option> element.
	        var option = document.createElement('option');
	        // Set the value using the item in the JSON array.
	        option.value = (item.country_name + " " + item.country_code);
	        // Add the <option> element to the <datalist>.
	        dataList.appendChild(option);
		});
	}
  })

document.getElementById('overlay').addEventListener("wheel", () => {
    document.getElementById('overlay').remove();
})

// differentiate between click and drag for map markers
let drag = false;

document.addEventListener('mousedown', () => drag = false);
document.addEventListener('mousemove', () => drag = true);
