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

function getTerrorismData() {
	var url = getAPIBaseURL() + '/world/'
	
	fetch(url, {method: 'get'})
	
	.then((response) => response.json())
	
	.then(function())//Figure out how to format data here
}


function hoverPopupTemplate(geography, data) {
	var attacks = 0;
	if (data && 'attacks' in data) {
		attacks = data.attacks;
	}
	
	
}

function onCountryClick(geography) {
	window.location = getAPIBaseUrl + '/' + geography.properties.name '/';
}
