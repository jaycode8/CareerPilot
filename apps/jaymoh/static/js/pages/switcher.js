// ltr-rtl
var isChangeMode = document.getElementById("ltr-rtl");
if (isChangeMode) {
    isChangeMode.addEventListener("click", function (e) {
        var themeMode = document.documentElement.getAttribute("dir");
        if (themeMode == "ltr") {
            document.documentElement.setAttribute("dir", "rtl");
        } else {
            document.documentElement.setAttribute("dir", "ltr");
        }

        swiperDir();
    });
}


// Swicher
function toggleSwitcher() {
    var i = document.getElementById('style-switcher');

    if (!i.classList.contains("show")) {
        i.classList.add("show")
    } else {
        i.classList.remove("show")
    }
};

// Light-dark
var isChangeMode = document.getElementById("mode");
if (isChangeMode) {
    isChangeMode.addEventListener("click", function (e) {
        var themeMode = document.documentElement.getAttribute("data-mode");
        if (themeMode == "light") {
            document.documentElement.setAttribute("data-mode", "dark");
        } else {
            document.documentElement.setAttribute("data-mode", "light");
        }
    });
}

// data-theme-color
document.querySelectorAll("#style-switcher li").forEach(function (item) {
    var layoutGetAttr = item.querySelector("a").getAttribute("data-color")
    if (sessionStorage.getItem("data-theme-color") && sessionStorage.getItem("data-theme-color") == layoutGetAttr) {
        document.documentElement.setAttribute('data-theme-color', layoutGetAttr);
    }
    if (document.documentElement.getAttribute('data-theme-color') == layoutGetAttr) {
        item.querySelector("a").classList.add("active");
    }
    item.querySelector("a").addEventListener("click", function () {
        sessionStorage.setItem("data-theme-color", layoutGetAttr);

        if (sessionStorage.getItem("data-theme-color") && sessionStorage.getItem("data-theme-color") == layoutGetAttr) {
            document.documentElement.setAttribute('data-theme-color', layoutGetAttr);
        }
        // link active
        var themecolorList = document.querySelector("#style-switcher li a.active");
        if (themecolorList) themecolorList.classList.remove("active");
        this.classList.add("active");
    })
})
