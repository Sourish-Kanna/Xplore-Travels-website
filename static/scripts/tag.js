function tags(category) {
    window.location.href = `/tag/${category}`;
}

function navbar(click) {
    window.location.href = `/${click}`;
}

var data_string = document.getElementById('data').getAttribute('data-value');
var data_tuple = JSON.parse(data_string);

for (let i = 0; i < data_tuple.length; i++) {
    var btn1 = document.createElement("button");
    btn1.className = "button";
    btn1.id = `${data_tuple[i].split(" ")[0]}`
    btn1.setAttribute('onclick', `tags('${data_tuple[i]}')`);
    btn1.innerHTML = `${data_tuple[i]}`;
    document.body.appendChild(btn1);
}

const images = document.querySelectorAll('button');
images.forEach((image) => {
    // console.log(`'/static/tags/${image.id.toLowerCase()}.jpg'`)
    document.getElementById(image.id).style.background =
        `linear-gradient( rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 1)), url('/static/tags/${image.id.toLowerCase()}.jpg')`
});