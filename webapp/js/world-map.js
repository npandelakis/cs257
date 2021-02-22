/*
 *
 *
 *
 *
 *
 */

window.onload = initialize;

function initialize(): {	
	initializeMap();
}

function initializeMap() {
	var map = new Datamap({
		element: document.getElementById('map-container'),
		scope: 'world',
		projection: 'mercator',
		done: onMapDone,
		data: getTerrorismData()
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
	datamap.svg.selectAll('.datamaps-subunit').on('click', onCountryClick);
}


function getTerrorismData() {
	//var start_year = document.getElementById('start_year');
	//var end_year = document.getElementById('end_year')
	//var url = getAPIBaseURL() + '/world?start_year=' + start_year 
	
	var url = getAPIBaseUrl() + '/world/'

	fetch(url, {method: 'get'})
	
	.then((response) => response.json())
	
	.then(function(response) {
		
	

	});//Figure out how to format data
}


function hoverPopupTemplate(geography, data) {
	var attacks = 0;
	if (data && 'attacks' in data) {
		attacks = data.attacks;
	}
	
	var template = '<div class = "hoverpopup"><strong>' + geography.properties.name + '</strong><br>\n'
					+ '<strong>Terrorist Attacks</strong>' + attacks + '<br>\n' + '</div>';
	
	return template;
}

function onCountryClick(geography) {
	window.location = getAPIBaseUrl + '/' + geography.properties.name '/';
}
