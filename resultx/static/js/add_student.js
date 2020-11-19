$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
<<<<<<< HEAD
    fdata.append('profile', 2);
=======
    fdata.append('profile', 1);
    fdata.append('subjects', $('#select').val());
>>>>>>> 1d1307486053c14515742e8c21894d0351dea52d
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
<<<<<<< HEAD
=======
});

$('.demo').dropdown({
    multipleMode: 'label',
>>>>>>> 1d1307486053c14515742e8c21894d0351dea52d
});