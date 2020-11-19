$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
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

function changeTeacher() {
    var x = $('.sub').val();
    $('.teacher').css({ 'display': 'none' });
    $('.' + x).css({ 'display': 'block' });
}
let data = {};
let data1 = [],
    data2 = [];

function addsubject() {
    data1.push($('.sub').val());
    data1.push($('.tech').val());
    $('#added').append("<div>" + $('.' + $('.sub').val()).html() + $('.tech').html() + "</div>");
    console.log(data1);
    console.log(data2);
}