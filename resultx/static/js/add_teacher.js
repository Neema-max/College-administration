$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
    fdata.append('profile', 2);
    fdata.append('subjects', $('#select').val());
    $.ajax({
        type: "POST",
        url: '.',
        data: fdata,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data.message);
            if (data.result == 'success') {
                window.location.href = '/dashboard/';
            } else {
                $('#error').html(data.message);
            }
        },
    });
});

$('.demo').dropdown({
    multipleMode: 'label',
});