
/********* dropdown common js *********/

var dropdownElem = document.querySelectorAll('.dropdown');
var dropupElem = document.querySelectorAll('.dropup');
var dropStartElem = document.querySelectorAll('.dropstart');
var dropendElem = document.querySelectorAll('.dropend');
var isShowDropMenu = false;
var isMenuInside = false;
// dropdown event
dropdownEvent(dropdownElem, 'bottom-start');
// dropup event
dropdownEvent(dropupElem, 'top-start');
// dropstart event
dropdownEvent(dropStartElem, 'left-start');
// dropend event
dropdownEvent(dropendElem, 'right-start');

function dropdownEvent(elem, place) {
    Array.from(elem).forEach(function (item) {
        item.querySelectorAll(".dropdown-toggle").forEach(function (subitem) {
            subitem.addEventListener("click", function (event) {
                subitem.classList.toggle("show");
                var popper = Popper.createPopper(subitem, item.querySelector(".dropdown-menu"), {
                    placement: place
                });

                if (subitem.classList.contains("show") != true) {
                    item.querySelector(".dropdown-menu").classList.remove("block")
                    item.querySelector(".dropdown-menu").classList.add("hidden")
                } else {
                    dismissDropdownMenu()
                    item.querySelector(".dropdown-menu").classList.add("block")
                    item.querySelector(".dropdown-menu").classList.remove("hidden")
                    if (item.querySelector(".dropdown-menu").classList.contains("block")) {
                        subitem.classList.add("show")
                    } else {
                        subitem.classList.remove("show")
                    }
                    event.stopPropagation();
                }

                isMenuInside = false;
            });
        });
    });
}

function dismissDropdownMenu() {
    Array.from(document.querySelectorAll(".dropdown-menu")).forEach(function (item) {
        item.classList.remove("block")
        item.classList.add("hidden")
    });
    Array.from(document.querySelectorAll(".dropdown-toggle")).forEach(function (item) {
        item.classList.remove("show")
    });
    isShowDropMenu = false;
}

// dropdown form
Array.from(document.querySelectorAll(".dropdown-menu")).forEach(function (item) {
    if (item.querySelectorAll("form")) {
        Array.from(item.querySelectorAll("form")).forEach(function (subitem) {
            subitem.addEventListener("click", function (event) {
                if (!isShowDropMenu) {
                    isShowDropMenu = true;
                }
            })
        });
    }
});

// data-tw-auto-close
Array.from(document.querySelectorAll(".dropdown-toggle")).forEach(function (item) {
    var elem = item.parentElement
    if (item.getAttribute('data-tw-auto-close') == 'outside') {
        elem.querySelector(".dropdown-menu").addEventListener("click", function () {
            if (!isShowDropMenu) {
                isShowDropMenu = true;
            }
        });
    } else if (item.getAttribute('data-tw-auto-close') == 'inside') {
        item.addEventListener("click", function () {
            isShowDropMenu = true;
            isMenuInside = true;
        });
        elem.querySelector(".dropdown-menu").addEventListener("click", function () {
            isShowDropMenu = false;
            isMenuInside = false;
        });
    }
});

window.addEventListener('click', function (e) {
    if (!isShowDropMenu && !isMenuInside) {
        dismissDropdownMenu();
    }
    isShowDropMenu = false;
});





/********* modal common js *********/
// openModal
var modalTrigger = document.querySelectorAll('[data-tw-toggle="modal"]');
var isModalShow = false;
Array.from(modalTrigger).forEach(function (item) {
    item.addEventListener("click", function () {
        var target = this.getAttribute('data-tw-target').substr(1);
        var modalWindow = document.getElementById(target);

        if (modalWindow.classList.contains("hidden")) {
            modalWindow.classList.remove('hidden');
            document.body.classList.add('overflow-hidden');
        } else {
            modalWindow.classList.add('hidden');
            document.body.classList.remove('overflow-hidden');
        }
        isModalShow = false;

        if (item.getAttribute('data-tw-backdrop') == 'static') {
            isModalShow = true;
        }
    });
});

// closeButton
var closeButton = document.querySelectorAll('[data-tw-dismiss="modal"]');
Array.from(closeButton).forEach(function (subElem) {
    subElem.addEventListener("click", function () {

        var modalWindow = subElem.closest(".modal");
        if (modalWindow.classList.contains("hidden")) {
            modalWindow.classList.remove('hidden');
            document.body.classList.add('overflow-hidden');
        } else {
            modalWindow.classList.add('hidden');
            document.body.classList.remove('overflow-hidden');
        }
    });
});

// closeModal
var modalElem = document.querySelectorAll('.modal');
Array.from(modalElem).forEach(function (elem) {

    // modalOverlay
    var modalOverlay = elem.querySelectorAll('.modal-overlay');
    Array.from(modalOverlay).forEach(function (subItem) {
        subItem.addEventListener("click", function () {
            if (!isModalShow) {
                if (elem.classList.contains("hidden")) {
                    elem.classList.remove('hidden');
                    document.body.classList.add('overflow-hidden');
                } else {
                    elem.classList.add('hidden');
                    document.body.classList.remove('overflow-hidden');
                }
            }
        });
    });

    // Escape
    document.addEventListener("keydown", function (event) {
        var key = event.key;
        if (!isModalShow) {
            if (key == "Escape") {
                elem.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
            }
        }
    });
});

