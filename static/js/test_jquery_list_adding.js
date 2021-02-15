counter = 1;

$(document).ready(function(){
    $('#the-href').on('click', function(){
        $('#the-list').append('<li>' + counter + '</li>');
        counter++
    });
});