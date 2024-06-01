var slideshow = document.getElementById('slideshow').getAttribute('data-value');
var data_tuple = JSON.parse(slideshow);

for (let i = 0; i < data_tuple.length; i++) {
    var div = document.createElement("div");
    div.className = "mySlides";
    var img = document.createElement("img");
    img.src = `/static/cities/${data_tuple[i].split(" ")[0].toLowerCase()}.jpg`;
    div.appendChild(img);
    document.getElementById('slideshow').appendChild(div);
}

var j = 0;
var icons = ['road', 'hotel', 'cutlery', 'camera', 'compass'];
var data_string = document.getElementById('data').getAttribute('data-value');
var data = JSON.parse(data_string);

var divFlyout = document.createElement('div');
divFlyout.id = 'flyout';
for (var key in data) {
    var divFlyoutMenu = document.createElement('div');
    divFlyoutMenu.className = 'flyout-menu';
    var iElement = document.createElement('i');
    iElement.className = 'fa fa-' + icons[j++];
    divFlyoutMenu.appendChild(iElement);
    var bElement = document.createElement('b');
    bElement.innerHTML = ' ' + key.charAt(0).toUpperCase() + key.slice(1);
    divFlyoutMenu.appendChild(bElement);
    var divContentMenu = document.createElement('div');
    divContentMenu.className = 'content-menu';
    if (typeof data[key] === 'object') {
        for (var key1 in data[key]) {
            var bElement = document.createElement('b');
            bElement.innerHTML = key1.charAt(0).toUpperCase() + key1.slice(1) + ': ';
            var ulElement = document.createElement('ul');
            var liElement = document.createElement('li');
            liElement.innerHTML = data[key][key1];
            ulElement.appendChild(bElement);
            ulElement.appendChild(liElement);
            divContentMenu.appendChild(ulElement);
            divFlyoutMenu.appendChild(divContentMenu);
        }
    } else {
        var divContentMenu = document.createElement('div');
        divContentMenu.className = 'content-menu';
        var ulElement = document.createElement('ul');
        var sights = data[key].split(', ');
        for (var i = 0; i < sights.length; i++) {
            var liElement = document.createElement('li');
            liElement.innerHTML = sights[i];
            ulElement.appendChild(liElement);
        }
        divContentMenu.appendChild(ulElement);
        divFlyoutMenu.appendChild(iElement);
        divFlyoutMenu.appendChild(bElement);
        divFlyoutMenu.appendChild(divContentMenu);
    }
    divFlyout.appendChild(divFlyoutMenu);
}
document.body.appendChild(divFlyout);

var aBack = document.createElement('a');
aBack.className = 'back';
aBack.href = '/tag';
aBack.innerHTML = 'Home';
document.body.appendChild(aBack);

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}