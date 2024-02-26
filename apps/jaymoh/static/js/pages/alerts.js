
/********* Alert common js *********/

// alert dismissible
if (document.querySelectorAll('.alert-dismissible')) {
    var alertDismiss = document.querySelectorAll('.alert-dismissible');

    Array.from(alertDismiss).forEach(function (item) {
        item.querySelector(".alert-close").addEventListener('click', function () {
            item.classList.add('hidden');
        });
    });
}
