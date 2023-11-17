
function redirectTologin(){
    window.location.href = "/lessons/sigin";
}
function redirectToregister(){
    window.location.href = "/lessons/signup";
}


function toggleMenu(){
	var menu = document.getElementById('mobile-menu');
	menu.classList.toggle("open");
	menu.classList.toggle("closeed");
	}