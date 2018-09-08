$(document).ready(function() {
    var site_base_url = 'http://localhost:5000';
    var refresh_interval = 2000;

    // button handler for help queue
    $("#help-queue-table").on('click', '.btn-floating', function () {
        var fn = $(this).parent().parent().data("first_name");
        var ln = $(this).parent().parent().data("last_name");
        var k = $(this).parent().parent().data("kerberos");
        console.log($(this).parent().parent());

        $.ajax({
            type: "POST",
            url: site_base_url + "/queue/help",
            data: 'first_name='+fn+'&last_name='+ln+'&kerberos='+k+'&remove=true'
        }).then(function(data) {
            console.log(data);
        });

        $(this).parent().parent().remove()
    });

    // button handler for checkoff queue
    $("#checkoff-queue-table").on('click', '.btn-floating', function () {
        var fn = $(this).parent().parent().data("first_name");
        var ln = $(this).parent().parent().data("last_name");
        var k = $(this).parent().parent().data("kerberos");
        console.log($(this).parent().parent());

        $.ajax({
            type: "POST",
            url: site_base_url + "/queue/checkoff",
            data: 'first_name='+fn+'&last_name='+ln+'&kerberos='+k+'&remove=true'
        }).then(function(data) {
            console.log(data);
        });

        $(this).parent().parent().remove()
    });


    // refresh the lab queue every `refresh_interval` seconds
    setInterval(function() {

            $.ajax({
                type: "GET",
                url: site_base_url + "/queue/help"
            }).then(function(data) {
            $('#help-queue-table').empty()
            if (data.message.length > 0) {console.log(data.message)};
            $.each(data.help_queue, function(i, item) {
                pulse = '';
                if (i == 0) {
                    pulse = 'pulse'
                };

                $('#help-queue-table').append(
                    $('<tr>').append(
                        $('<td>').text(item[0] + " " + item[1][0]),
                        $('<td>').text(item[2]),
                        $('<td>').append(
                            $('<a>').addClass("btn-floating btn-small waves-effect waves-light red "+pulse).append(
                                $('<i>').addClass("material-icons").text('remove')
                            )
                        )
                    ).data('first_name', item[0]).data('last_name', item[1]).data('kerberos', item[2])
                );
            });
        });

            $.ajax({
                type: "GET",
                url: site_base_url + "/queue/checkoff"
            }).then(function(data) {
            $('#checkoff-queue-table').empty()
            if (data.message.length > 0) {console.log(data.message)};
            $.each(data.checkoff_queue, function(i, item) {
                pulse = '';
                if (i == 0) {
                    pulse = 'pulse'
                };

                $('#checkoff-queue-table').append(
                    $('<tr>').append(
                        $('<td>').text(item[0] + " " + item[1][0]),
                        $('<td>').text(item[2]),
                        $('<td>').append(
                            $('<a>').addClass("btn-floating btn-small waves-effect waves-light red "+pulse).append(
                                $('<i>').addClass("material-icons").text('remove')
                            )
                        )
                    ).data('first_name', item[0]).data('last_name', item[1]).data('kerberos', item[2])
                );
            });
        });

    }, refresh_interval);

});