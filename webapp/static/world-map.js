/* world-map.js
 *
 * Javascript to query the /api/world/ endpoint
 * and display the data on a world map.
 *
 * Written by Nick Pandelakis and Grace de Benedetti
 */

window.onload = initialize;

function initialize() {
	initializeMap();
}

async function initializeMap() {

	var mapData = await getTerrorismData();

	var map = new Datamap({
		element: document.getElementById('map-container'),
		scope: 'world',
		projection: 'equirectangular',
		done: onMapDone,
		data: mapData,
		fills: { defaultFill:'#999999' },
		geographyConfig: {
			popupTemplate: hoverPopupTemplate,
			borderColor: '#eeeeee',
			higlightFillColor: '#99dd99',
			highlightBorderColor: '#000000'
		}

	});

	const filterButton = document.getElementById("filter-button");

	filterButton.addEventListener("click", async function() {
		var mapDataNew = await getTerrorismData();
		console.log(mapDataNew)
		map.updateChoropleth(mapDataNew);
	})
}

function onMapDone(dataMap) {
	dataMap.svg.selectAll('.datamaps-subunit').on('click', onCountryClick);
}


async function getTerrorismData(callback) {
	var start_year = document.getElementById('start_year');
	var end_year = document.getElementById('end_year')

	if (start_year.value && end_year.value) {
		var url = getAPIBaseUrl() + 'api/world?start_year=' + start_year.value
			  + '&end_year=' + end_year.value
	} else {
		var url = getAPIBaseUrl() + 'api/world';
	}

	const response = await fetch(url);

	return response.json();

}

function hoverPopupTemplate(geography, data) {
	var attacks = 0;
	if (data && 'number_of_attacks' in data) {
		attacks = data.number_of_attacks;
	}

	var template = '<div class = "hoverpopup"><strong>' + geography.properties.name + '</strong><br>\n'
					+ '<strong>Terrorist Attacks: </strong>' + attacks + '<br>\n' + '</div>';

	return template;
}

function onCountryClick(data) {

	window.location = 'countries/' + data.id.toLowerCase();
}

function getAPIBaseUrl() {
	var getUrl = window.location;
	var baseUrl = getUrl.protocol + '//' + getUrl.host + '/';
	return baseUrl;
}

document.addEventListener("DOMContentLoaded", function() {
	const clearIcon = document.querySelector(".clear-icon");
	const searchBar = document.querySelector(".search");
	const button = document.getElementById("search-button");

	searchBar.addEventListener("keyup", () => {
	  if(searchBar.value && clearIcon.style.visibility != "visible"){
	    clearIcon.style.visibility = "visible";
	  } else if(!searchBar.value) {
	    clearIcon.style.visibility = "hidden";
	  }
	});

	clearIcon.addEventListener("click", () => {
	  searchBar.value = "";
	  clearIcon.style.visibility = "hidden";
	});

	button.addEventListener("click", () => {
		window.location = 'countries/' + searchBar.value;
	})

})
