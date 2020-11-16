$(document).on('submit', '#submit', function(e) {
    alert(1);
    e.preventDefault();
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
    fdata.append('profile', 3);
    $.ajax({
        type: "POST",
        url: '.',
        data: fdata,
        processData: false,
        contentType: false,
        success: function(data) {
            alert(2);
            if (data.result == 'success') {
                console.log(1);
                window.location.href = '/dashboard/';
            } else {
                $('#error').html(data.message);
            }
        },
    });
});