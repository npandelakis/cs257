/* world-map.js
 *
 * Javascript to query the /api/world/ endpoint
 * and display the data on a world map.
 *
 * Written by Nick Pandelakis and Grace de Benedetti
 */

window.onload = initialize;
var dataListValues = [];

const NO_COUNTRY_CLICK = ['GRL', 'MNG', '-99', 'PRI', 'OMN', 'GNB','SVK','GUF','ESH','ZWE','RUS','COD','COG'];

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
	dataMap.svg.selectAll('.datamaps-subunit')
	.filter( function(data) {

			if (NO_COUNTRY_CLICK.includes(data.id)) {
					return false;
			} else {
					return true;
			}
	})
	.on('click', onCountryClick);
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

	if (NO_COUNTRY_CLICK.includes(geography.id)) {
			var template = '<div class = "hoverpopup"><strong>' + geography.properties.name + '(' + geography.id + ')' + '</strong><br>\n'
							+ '<strong>Terrorist Attacks: </strong>' + attacks + '<br>\n'

	} else {
			var template = '<div class = "hoverpopup"><strong>' + geography.properties.name + '(' + geography.id + ')' + '</strong><br>\n'
							+ '<strong>Terrorist Attacks: </strong>' + attacks + '<br>\n'
							+ 'Click to Learn More!' + '<br>\n' + '</div>';
	}

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

//search
document.addEventListener("DOMContentLoaded", function() {
	//const searchBar = document.querySelector("nav.navbar.navbar-expand-md.navbar-dark.bg-dark.fixed-top.div.container-fluid.div.collapse.navbar-collapse.ul.navbar-nav.me-auto.mb-2.mb-md-0.form.d-flex");
	//const searchBar = document.querySelector("nav > div.container-fluid > div.collapse.navbar-collapse > ul.navbar-nav.me-auto.mb-2.mb-md-0 > form.d-flex");
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
			if (option.value in dataListValues){
				dataList.removeChild(option);
			}
			else{
	        // Add the <option> element to the <datalist>.
	        dataList.appendChild(option);
			dataListValues.push(option.value);
		}
		});
	}
  })
