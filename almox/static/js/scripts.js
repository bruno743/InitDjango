$(document).ready(function() {
    var search = $('#search-btn');
    var text = $('#search-form');

    $(search).on('click', function() {
        text.submit();
    });
})