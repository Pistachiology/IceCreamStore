$(document).ready(function(){
    var delay = 800;
    $(".flash-notification").each(function( index ){
        var noti = this;
        setTimeout(function (){ $(noti).slideUp(800, function(){}); }, delay);
        delay = delay + 800;
    });
});
function setAndShowNotificationBar(message){
    $("div#notification-text").html(message);
    $("#notification_bar").fadeOut().fadeIn();
    setTimeout(function(){
        $("#notification_bar").slideUp(1000, function (){});
    });
} 
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = getCookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
