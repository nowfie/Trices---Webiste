const navbar = document.querySelector('#navmain');
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    if (scrollPosition > 100) {
        navbar.style.backgroundColor = '#1e1d22';
    } else {
        navbar.style.backgroundColor = 'transparent';
    }
});

function active(link) {
    var links = document.getElementsByClassName('nav-link')

    for (var i = 0; i < links.length; i++) {
        links[i].classList.remove('active')
    }

    link.classList.add('active')
}
//
//document.addEventListener('DOMContentLoaded', function() {
//    var video = document.getElementById('background-video');
//
//    window.addEventListener('scroll', function() {
//        var scrollPos = window.scrollY || window.scrollTop || document.documentElement.scrollTop;
//
//        var scaleFactor = 1 + scrollPos / 1000;
//        video.style.transform = 'translate(-50%, -50%) scale(' + scaleFactor + ')';
//    });
//});