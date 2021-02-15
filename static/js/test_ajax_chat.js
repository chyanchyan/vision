var msg = document.currentScript.getAttribute('msg_url');

function updateMsg(){
    console.log('req-ing JSON');
    $.getJSON(msg, function(rowz){
        console.log('JSON', rowz);
        $('#chatcontent').empty();
        for (var i = 0; i < rowz.length; i++){
            arow = rowz[i];
            $('#chatcontent').append('<p>' + arow[0] +
                '<br/>&nbsp;&nbsp;' + arow[1] + '</p>\n');
        }
        setTimeout('updateMsg()', 4000);
    });
};


$(document).ready(function(){
    $.ajaxSetup({ cache: false});
    updateMsg();
});
