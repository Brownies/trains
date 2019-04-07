"use strict";

function make_request() {
    let xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("GET", "");
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    xhr.onload = function(){update_table(xhr)};
    xhr.send();
}


function update_table(xhr) {
    if (xhr.status === 200) {
        let old_body = document.getElementById("trains");
        let new_body = document.createElement("tbody");
        new_body.setAttribute("id", "trains");

        for (let i in xhr.response) {
            let row = document.createElement("tr");
            let train = xhr.response[i];
            for (let j in train) {
                let attribute = train[j];
                let td = document.createElement("td");
                td.innerHTML = attribute;
                row.appendChild(td);
            }
            new_body.appendChild(row);
        }
        old_body.parentNode.replaceChild(new_body, old_body);
    }
}

let timer = setInterval(make_request, 5000);

function update_timer() {
    let time = document.getElementById("timer_select").value;
    clearTimeout(timer);
    timer = setInterval(make_request, time * 1000);
}