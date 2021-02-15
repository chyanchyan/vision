$(document).ready(function(){
    $('#tog').on('click', function(){
        $('#spinner').toggle();
    });
    $('#red').on('click', function(){
        $('#para').css('background-color', 'red');
    });
});
