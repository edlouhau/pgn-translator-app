//Auto submit the source language form.
const textarea = document.getElementById('id_game');
const form = document.getElementById('sourceForm');
let delayTimer;

textarea.addEventListener('input', function () {
    clearTimeout(delayTimer);
    delayTimer = setTimeout(function () {
        form.submit();
    }, 500); // Set a delay of 1000 milliseconds (1 second)
});