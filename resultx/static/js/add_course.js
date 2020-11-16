$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
    console.log(fdata);
    $.ajax({
        type: "POST",
        url: '.',
        data: fdata,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data.message);
            if (data.result == 'success') {
                if (data.admin == 'false')
                    window.location.href = '/dashboard/';
            } else {
                $('#error').html(data.message);
            }
        },
    });
});