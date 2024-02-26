//
/********************* Counter js ************************/
//

function _toConsumableArray(arr) {
  if (Array.isArray(arr)) {
    for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) {
      arr2[i] = arr[i];
    }
    return arr2;
  } else {
    return Array.from(arr);
  }
}

var isCounters = document.querySelectorAll(".counter");

isCounters.forEach(function (value) {
  var patt = /(\D+)?(\d+)(\D+)?(\d+)?(\D+)?/;
  var time = 1000;
  var result = [].concat(_toConsumableArray(patt.exec(value.textContent)));
  var fresh = true;
  var ticks;

  result.shift();

  result = result.filter(function (res) {
    return res != null;
  });

  while (value.firstChild) {
    value.removeChild(value.firstChild);
  }
  result.forEach(function (res) {
    if (isNaN(res)) {
      value.insertAdjacentHTML("beforeend", "<span>" + res + "</span>");
    } else {
      for (var i = 0; i < res.length; i++) {
        value.insertAdjacentHTML(
          "beforeend",
          '<span data-value="' +
            res[i] +
            '">\n\t\t\t\t\t\t<span>&ndash;</span>\n\t\t\t\t\t\t' +
            Array(parseInt(res[i]) + 1)
              .join(0)
              .split(0)
              .map(function (x, j) {
                return "\n\t\t\t\t\t\t\t<span>" + j + "</span>\n\t\t\t\t\t\t";
              })
              .join("") +
            "\n\t\t\t\t\t</span>"
        );
      }
    }
  });

  ticks = [].concat(
    _toConsumableArray(value.querySelectorAll("span[data-value]"))
  );

  var activate = function () {
    var top = value.getBoundingClientRect().top;
    var offset = window.innerHeight * 0.8;

    setTimeout(function () {
      fresh = false;
    }, time);
    if (top < offset) {
      setTimeout(function () {
        ticks.forEach(
          function (tick) {
            var dist = parseInt(tick.getAttribute("data-value")) + 1;
            tick.style.transform = "translateY(-" + dist * 100 + "%)";
          },
          fresh ? time : 0
        );
      });
      window.removeEventListener("scroll", activate);
    }
  };
  window.addEventListener("scroll", activate);
  activate();
});
