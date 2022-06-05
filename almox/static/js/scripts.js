$(document).ready(function() {
    var search = $('#search-btn');
    var text = $('#search-form');

    var filter = $('#filter-btn');
    var fields = $('#filter-form');

    $(search).on('click', function() {
        text.submit();
    });

    $(filter).on('click', function() {
        fields.submit();
    });
})