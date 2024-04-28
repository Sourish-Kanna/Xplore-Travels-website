var data_string = document.getElementById('slideshow').getAttribute('data-value');
var data_tuple = JSON.parse(data_string);
for (let i = 0; i < data_tuple.length; i++) {
    var div = document.createElement("div");
    div.className = "mySlides";
    var img = document.createElement("img");
    img.src = `/static/cities/${data_tuple[i].split(" ")[0]}.jpg`;
    div.appendChild(img);
    document.getElementById('slideshow').appendChild(div);
    // console.log(`${data_tuple[i].split(" ")[0]}`);
}

var aBack = document.createElement('a');
aBack.className = 'back';
aBack.href = '/tag';
aBack.innerHTML = 'Back';
document.body.appendChild(aBack);

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    // console.log(slides);
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 4000); // Change image every 4 seconds
}