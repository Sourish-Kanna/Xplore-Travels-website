var user = document.getElementById("cities").textContent;
var hello = document.getElementById("pname")
var items = document.getElementById("points");
var newElement1 = document.createElement('li');
if (user == "Iphone15") {
    hello.innerHTML = "Iphone 15"
    items.innerHTML = "<li>Periscope camera</li>"+"<li>5G connectivity</li>"+"<li>120Hz ProMotion display</li>"+"<li>Improved battery life</li>"+"<li>Enhanced A16 Bionic chip</li>"+"<li>Stainless steel frame</li>"+"<li>Improved Face ID</li>"+"<li>LiDAR scanner</li>"+"<li>Improved Night mode</li>"+"<li>Improved Smart HDR 4</li>"+"<li>Improved Deep Fusion</li>"+"<li>Improved Portrait mode</li>"+"<li>Improved Cinematic mode</li>"+"<li>Improved ProRes video recording</li>";
} else if (user == "OnePlus9") {
    hello.innerHTML= "OnePlus 9"
    items.innerHTML = "<li>50MP camera</li>"+"<li>5G connectivity</li><li>120Hz AMOLED display</li><li>4500mAh battery with 65W fast charging</li><li>Qualcomm Snapdragon 888 processor</li><li>Aluminum frame</li><li>Improved face recognition</li><li>Improved fingerprint sensor</li><li>Improved night mode</li><li>Improved portrait mode</li><li>Improved video stabilization</li><li>Improved audio quality</li><li>Improved haptic feedback</li><li>Improved gaming performance</li><li>Improved cooling system</li>";
} else if (user == "Mi12Pro") {
    hello.innerHTML= "Xiaomi 12 Pro"
    items.innerHTML = "<li>108MP camera</li><li>5G connectivity</li><li>120Hz AMOLED display</li><li>4500mAh battery with 120W fast charging</li><li>Qualcomm Snapdragon 8 Gen 1 processor</li><li>Stainless steel frame</li><li>Improved face recognition</li><li>Improved fingerprint sensor</li><li>Improved night mode</li><li>Improved portrait mode</li><li>Improved video stabilization</li><li>Improved audio quality</li><li>Improved haptic feedback</li><li>Improved gaming performance</li><li>Improved cooling system</li>";
} else if (user == "oppof21pro") {
    hello.innerHTML= "Oppo F21 Pro"
    items.innerHTML = "<li>64MP camera</li><li>5G connectivity</li><li>6.43-inch AMOLED display</li><li>4500mAh battery with 33W fast charging</li><li>Qualcomm Snapdragon 680 processor</li><li>Plastic frame</li><li>Improved face recognition</li><li>Improved fingerprint sensor</li><li>Improved night mode</li><li>Improved portrait mode</li><li>Improved video stabilization</li><li>Improved audio quality</li><li>Improved haptic feedback</li><li>Improved gaming performance</li><li>Improved cooling system</li>";
}

