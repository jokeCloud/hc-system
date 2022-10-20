/* ------------------------------------------------------
# All the scripts here it will extends to all the pages
------------------------------------------------------ */

// 1) Script to validate all inputs
function validateEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll() {
    var name = $("#name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var age = $("#age").val();
    var gender = $("#gender").val();

    if (name == '') {
        swal("Opss =|", "Name field cannot be empty", "error");
        return false;
    }
    //force users to input the last name
    else if (name.split(' ').length < 2) {
        swal("Opss =|", "The last name is required.", "error");
        return false;
    }
    else if (name == name.toUpperCase()) {
        swal("Opss =|", "Name field be cannot uppercase", "error");
        $("#name").val("");
        return false;
    }
    else if (phone == '') {
        swal("Opss =|", "Phone field cannot be empty", "error");
        return false;
    }
    else if (email == '') {
        swal("Opss =|", "Email field cannot be empty", "error");
        return false;
    }
    else if (!(validateEmail(email))) {
        swal("Opss =|", "Age field cannot be empty", "error");
        return false;
    }
    else if (age == '') {
        swal("Opss =|", "Age field cannot be empty", "error");
        return false;
    }
    //else if (age > 120) {
    //    swal("Denied =|", "The maximun age is 120 years old.", "error");
    //    $("#age").val("");
    //    return false;
    //}
    else if (gender == '') {
        swal("Opss =|", "Gender field cannot be empty", "error");
        return false;
    }
    else {
        return true;
    }
}
$("#btn-add").bind("click", validateAll);

// 2) Script {Name field} only letter is allowed
$(document).ready(function () {
    // Only letter
    jQuery('input[name="name').keyup(function () {
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });
    // prevent stating with space
    $("input").on("keypress", function (e) {
        if (e.which === 32 && !this.value.length)
            e.preventDefault();
    });
});

// 3) Script to put First Letter captalized
$("#name").keyup(function () {
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function ($1) { return $1.toUpperCase(); }));
});

// 4) Script to LOWERCASE input email
$(document).ready(function () {
    $('#email').keyup(function () {
        this.value = this.value.toLowerCase();
    });
});


// 5) Script to allow only number age
$("#age").keyup(function () {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    };
});


// 6) Phone mask
$(document).ready(function () {
    $("#phone").inputmask("(99) 99999-9999", {
        "onincomplete": function () {
            swal("Opss.. =|", "Incomplete phone. Review.", "error");
            return false;
        }
    });
});


// 7) if input age has number greater than 120, auto clear(alternative option)
$(document).ready(function () {
    $("#age").keyup(function () {
        var age = $("#age").val();
        if (age > 120) {
            $("#age").val("");
            return false;
        }
    });
});


// 8) Prevent starting by zero in age field
$("#age").on("input", function () {
    if (/^0/.test(this.value)) {
        this.value = this.value.replace(/^0/, "")
    }
})

// 9) Prevent users registering fullname
$(document).ready(function () {
    $("#name").keyup(function () {
        var name = $("#name").val();
        if (name.split(' ').length == 3) {
            swal("Opss!", "Put only first and last name.", "info");
            $("#name").val("");
        }
    });
});

// 10) Time running at realtime
setInterval(function () {
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);

// 11) if no patient, show a message
var verify = $("#chk-td").length;
if (verify == 0) {
    $("#no-data").text("No patient found");
}

