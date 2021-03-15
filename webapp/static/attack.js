/* attack.js
 *
 * Javascript to query the /api/attack/<attack_id> endpoint
 * and display data on given attack.
 *
 * Written by Nick Pandelakis and Grace de Benedetti
 */

window.onload = initialize;

function initialize() {
    renderAttackInformation();
}


function renderAttackInformation() {



    url = getAPIBaseUrl() + 'api/attack/' + getAttackId();
    fetch(url)
    .then((response) => response.json())
    .then(function(data) {
        attack = data;

        console.log(attack)

        let header = document.createElement("h1");
        header.innerHTML = "Attack #" + attack.id.toString();
        document.body.appendChild(header);

        let ul = document.createElement("ul");

        for (var key in attack) {
            if (attack[key] == "None") {
                var li = document.createElement("li");
                li.innerHTML = key + " : Unknown";
                ul.appendChild(li);
            } else {
                var li = document.createElement("li");
                li.innerHTML = key + " : " + attack[key];
                ul.appendChild(li);
            }
        }

        document.body.appendChild(ul)


    })

}




function getAPIBaseUrl() {
    var getUrl = window.location;
    var baseUrl = getUrl.protocol + '//' + getUrl.host + '/';
    return baseUrl;
}

function getAttackId() {
    var pathname = window.location.pathname;
    return pathname.split('/').pop();
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
