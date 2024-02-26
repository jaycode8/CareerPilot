// 
// nav-tabs
// 
document.querySelectorAll(".nav-tabs").forEach(function (elem) {
    elem.querySelectorAll('[data-tw-toggle="tab"]').forEach(function (item) {
        item.addEventListener("click", function () {
            var tabID = item.getAttribute("data-tw-target");
            var tabContents = elem.querySelectorAll(".tab-content > .tab-pane");

            var activeElem = elem.querySelector('[data-tw-toggle="tab"].active');
            if (activeElem) activeElem.classList.remove("active");


            // clear value
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.add("hidden");
                tabContents[i].classList.remove("block");
            }

            // change value
            item.classList.add("active");
            document.getElementById(tabID).classList.remove("hidden");
            document.getElementById(tabID).classList.add("block");
        });
    });
});


// 
// accordion
// 
document.querySelectorAll('[data-tw-accordion="collapse"]').forEach(function (elem) {
    elem.querySelectorAll(".accordion-item").forEach(function (item) {
        item.querySelector(".accordion-header").addEventListener("click", function (event) {
            item.querySelector(".accordion-header").classList.toggle("active");

            if (item.querySelector(".accordion-header").classList.contains("active") != true) {
                item.querySelector(".accordion-body").classList.remove("block")
                item.querySelector(".accordion-body").classList.add("hidden")
            } else {
                dismissCollapse(elem)
                item.querySelector(".accordion-body").classList.add("block")
                item.querySelector(".accordion-body").classList.remove("hidden")
                if (item.querySelector(".accordion-body").classList.contains("block")) {
                    item.querySelector(".accordion-header").classList.add("active")
                } else {
                    item.querySelector(".accordion-header").classList.remove("active")
                }
                event.stopPropagation();
            }
        });
    });
});

function dismissCollapse(test) {
    Array.from(test.querySelectorAll(".accordion-body")).forEach(function (item) {
        item.classList.remove("block")
        item.classList.add("hidden")
    });
    Array.from(test.querySelectorAll(".accordion-header")).forEach(function (item) {
        item.classList.remove("active")
    });
}