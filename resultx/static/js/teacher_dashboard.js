$(document).on('submit', '#logout', function(e) {
    alert(1);
    e.preventDefault();
    $.ajax({
        type: "POST",
        url: '/logout/',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function() {
            window.location.href = '/';
        },
    });
});