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
