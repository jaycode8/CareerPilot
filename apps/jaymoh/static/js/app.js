

/********************* Menu Js **********************/

//  Window scroll sticky class add
function windowScroll() {
    const navbar = document.getElementById("navbar");
    if (
        document.body.scrollTop >= 50 ||
        document.documentElement.scrollTop >= 50
    ) {
        navbar.classList.add( "shadow", "nav-sticky");
    } else {
        navbar.classList.remove( "shadow", "nav-sticky");
    }
}

window.addEventListener('scroll', (ev) => {
    ev.preventDefault();
    windowScroll();
})


//menu active & scrollspy
var sections = document.querySelectorAll('.section');
window.onscroll = function () {
    var scrollPos = document.documentElement.scrollTop || document.body.scrollTop;
    for (var elem in sections) {
        if (sections.hasOwnProperty(elem) && (sections[elem].offsetTop - 105) <= scrollPos) {
            var id = sections[elem].id;
            if (id) {
                document.querySelector('#navbar .navbar-nav .active').classList.remove('active');
                document.querySelector('#navbar .navbar-nav .nav-link[href*=' + id + ']').parentNode.classList.add('active');
            }
        }
    }
};

function initActiveMenu() {
    var currentPath = location.pathname == "/" ? "index.html" : location.pathname.substring(1);
    currentPath = currentPath.substring(currentPath.lastIndexOf("/") + 1);
    if (currentPath) {
        var a = document.getElementById("navigation-menu").querySelector('li a[href="' + currentPath + '"]');
        if (a) {
            a.classList.add("active");
            var parentCollapseDiv = a.closest(".dropdown-menu");
            if (parentCollapseDiv) {
                if (parentCollapseDiv.parentElement.classList.contains('dropdown')) {
                    parentCollapseDiv.parentElement.children[0].classList.add("active");
                    console.log("test", parentCollapseDiv.parentElement)
                    if (parentCollapseDiv.parentElement.classList.contains('dropdown')) {
                        parentCollapseDiv.parentElement.children[0].classList.add("active");
                    }
                }
            }
        }
    }
}

// navbar toggler
document.getElementById("navbar").querySelector(".navbar-toggler").addEventListener("click", function () {
    var getAttr = this.getAttribute("data-collapse-toggle");
    if (document.getElementById(getAttr).classList.contains("hidden")) {
        document.getElementById(getAttr).classList.remove("hidden");
    } else {
        document.getElementById(getAttr).classList.add("hidden");
    }
});

window.addEventListener('resize', function(){
    document.getElementById('navbar-collapse').classList.add("hidden");
});


initActiveMenu();