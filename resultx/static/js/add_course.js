var data1 = [],
    data2 = [];
$(document).on('submit', '#submit', function(e) {
    e.preventDefault();
    alert(1);
    var fd1 = [],
        fd2 = [];
    for (var i = 0; i < data1.length; i++) {
        if (data1[i] != -1) {
            fd1.push(data1[i]);
            fd2.push(data2[i]);
        }
    }
    alert(fd1);
    alert(fd2);
    let dataa = document.getElementById('submit');
    let fdata = new FormData(dataa);
    fdata.append('teachers', fd2);
    fdata.append('subjects', fd1);
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
var x = 1024;

function addsubject() {
    alert(1);
    data1.push($('.sub').val());
    data2.push($('.teach').val());
    $('#added').append("<div id = " + x + ' onclick="deletesub(' + x + ')" >' + $('#' + $('.sub').val()).html() + $('#' + $('.teach').val() + '_teacher').html() + "</div>");
    x++;
    console.log(data1);
    console.log(data2);
}

function deletesub(x) {
    var index = x - 1024;
    data1[index] = -1;
    data2[index] = -1;
    $('#' + x.toString()).remove();
}