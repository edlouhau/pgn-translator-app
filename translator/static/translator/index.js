const textarea = document.getElementById('id_game');
const form = document.getElementById('forms');
const sourceDropdown = document.getElementById('id_source_lang_choices');
const targetDropdown = document.getElementById('id_target_lang_choices');
let delayTimer;

//Auto submit the source language form.
textarea.addEventListener('input', function () {
    clearTimeout(delayTimer);
    delayTimer = setTimeout(function () {
        form.submit();
    }, 500); // Set a delay of 1000 milliseconds (1 second)
});

//Auto submit selections from dropdown menus.
sourceDropdown.addEventListener('change', function() {
    form.submit();
});

targetDropdown.addEventListener('change', function() {
    form.submit();
});