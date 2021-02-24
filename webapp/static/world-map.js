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

	const mapData = await getTerrorismData();

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
}

function onMapDone(dataMap) {
	dataMap.svg.selectAll('.datamaps-subunit').on('click', onCountryClick);
}


async function getTerrorismData(callback) {
	var start_year = document.getElementById('start_year');
	var end_year = document.getElementById('end_year')
	//var url = getAPIBaseURL() + '/world?start_year=' + start_year
	//	  + '&end_year =' + end_year
	var url = 'http://localhost:5000/api/world';

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

function onCountryClick(geography) {
//	window.location = getAPIBaseUrl + '/' + geography.properties.name '/';
}

function getAPIBaseUrl() {

}
