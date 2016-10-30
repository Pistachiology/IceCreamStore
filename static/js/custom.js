$(document).ready(function(){
    var delay = 500;
    $(".flash-notification").each(function( index ){
        var noti = this;
        setTimeout(function (){ $(noti).slideUp(500, function(){}); }, delay);
        delay = delay + 500;
    });
});
