$("#id_username").keyup(function () {
    var username = $(this).val();
    var thisObject = this

    $.ajax({
        url: '../app/ajax/check-username',
        dataType: 'json',
        data: {
            "username": username
        },
        success: function (data) {
            $(thisObject).nextAll().remove();
            if (data.is_taken) {
                $(thisObject).after("<b style='color: red; '>&emsp;" + data.error_message + "</b>");
            }
        }
    })
});