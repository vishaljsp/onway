// blog page   form hel admision form 
function validate() {
    let name = $("#name").val();
    let email = $("#email").val();
    let number = $("#number").val();
    let menu_corce = $("#menu_corce").val();
    let ms = $("#message").val()

    console.log(ms)
    if (name === "") {
        $("#nameeer").text("Name is required!");
    }

    else if (email === "") {
        $("#emailerr").text("Email address is required!");
    }

    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#emailerr").text("Please enter a valid email address!");
    }

    else if (number === "") {
        $("#numbererr").text("Number is required!");
    }

    else if (number.length !== 10) {
        $("#numbererr").text("Please enter a valid 10-digit number!");
    }

    else if (menu_corce === "") {
        $("#menuerr").text("Menu course is required!");
    }
    else {
        $.ajax({
            type: "post",
            url: "/adminsion_data_form",
            data: {
                name: name,
                email: email,
                num: number,
                course: menu_corce,
                mass: ms,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Admission Form",
                    text: "Form submit successfully",
                    icon: "success",
                    button: "continue",
                });
            }

        })
    }
}


// contact  form 
function c_validate() {
    let name = $("#c_name").val()
    let email = $("#c_email").val()
    let mss = $("#c_mss").val()

    if (name === "") {
        $("#cerr").text("Name is required!");
    }

    else if (email === "") {
        $("#cerr").text("Email address is required!");
    }

    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#cerr").text("Please enter a valid email address!");
    }
    else if (mss === "") {
        $("#cerr").text("Message address is required!");

    }
    else {
        $.ajax({
            type: "post",
            url: "/contact",
            data: {
                name: name,
                email: email,
                massage: mss,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Thenks For Contact US",
                    text: "Form submit successfully",
                    icon: "success",
                    button: "continue",
                });
            }

        })
    }
}

// online apply form 

function apply_form_admition() {

    let name = $("#name").val();
    let number = $("#phone").val();
    let email = $("#email").val();
    let menu_corce = $("#menu_corse").val();
    let ms = $("#message").val()
    let image = $("#image").prop("files")[0];



    if (name === "") {
        $("#nm_err").text("Name is required!");
    }

    else if (email === "") {
        $("#email_err").text("Email address is required!");
    }

    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#email_err").text("Please enter a valid email address!");
    }

    else if (number === "") {
        $("#phone_err").text("Number is required!");
    }

    else if (number.length !== 10) {
        $("#phone_err").text("Please enter a valid 10-digit number!");
    }
    else {
        $.ajax({
            type: "post",
            url: "/apply-online",
            data: {
                name: name,
                email: email,
                num: number,
                course: menu_corce,
                mass: ms,
                img: image.name,

                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Admission Form",
                    text: "Form submit successfully",
                    icon: "success",
                    button: "continue",
                }).then(() => {
                    location.reload()


                })
            }

        })
    }
}


// quick form 

function quick0() {

    let name = $("#q_name").val();
    let number = $("#q_num").val();
    let email = $("#q_email").val();
    let cors = $("#q_course_menu").val();


    if (name === "") {
        $("#allnperr").text("Name is required!");
    }

    else if (email === "") {
        $("#allnperr").text("Email address is required!");
    }

    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#allnperr").text("Please enter a valid email address!");
    }

    else if (number === "") {
        $("#allnperr").text("Number is required!");
    }

    else if (number.length !== 10) {
        $("#allnperr").text("Please enter a valid 10-digit number!");
    }
    else if (cors === "") {
        $("#allnperr").text("Course is required!");
    }
    else {
        $.ajax({
            type: "post",
            url: "/mbbs-in-india",
            data: {
                name: name,
                email: email,
                num: number,
                cors: cors,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Admission Form",
                    text: "Form submit successfully",
                    icon: "success",
                    button: "continue",
                }).then(() => {
                    location.reload()


                })
            }

        })
    }
}


// bhms india form like quick form 

function bhms() {

    let name = $("#name").val();
    let number = $("#num").val();
    let email = $("#email").val();
    let cors = $("#course_menu").val();



    if (name === "") {
        $("#allnperr").text("Name is required!");
    }

    else if (email === "") {
        $("#allnperr").text("Email address is required!");
    }

    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#allnperr").text("Please enter a valid email address!");
    }

    else if (number === "") {
        $("#allnperr").text("Number is required!");
    }

    else if (number.length !== 10) {
        $("#allnperr").text("Please enter a valid 10-digit number!");
    }
    else if (cors === "") {
        $("#allnperr").text("Course is required!");
    }
    else {
        $.ajax({
            type: "post",
            url: "/study-bhms-in-india",
            data: {
                name: name,
                email: email,
                num: number,
                cors: cors,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Admission Form",
                    text: "Form submit successfully",
                    icon: "success",
                    button: "continue",
                }).then(() => {
                    location.reload()


                })
            }

        })
    }
}


function cument() {
    let coment = $("#coment").val();
    let name = $("#name").val();
    let email = $("#email").val();
    let web = $("#web").val();

    if (coment === "") {
        $("#xmerr").text("Comment is required!");
    }
    else if (name === "") {
        $("#xmerr").text("Name is required!");
    }
    else if (email === "") {
        $("#xmerr").text("Email address is required!");
    }
    else if (!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        $("#xmerr").text("Please enter a valid email address!");
    }
    else if (web === "") {
        $("#xmerr").text("web is required!");
    }
    else {
        $.ajax({
            type: "post",
            url: "/adminsion_data_form",

            data: {
                name: name,
                email: email,
                web: web,
                coment: coment,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (data) {
                swal({
                    title: "Comment Send Successfully 😊",
                    icon: "success",
                    button: "continue",
                }).then(() => {
                    location.reload()
                })
            }

        })
    }
}

// relative post 
function reletivpost(id) {
    $.ajax({
        type: "post",
        url: "/adminsion_data_form",
        data: {
            cat_id_relative_post:id,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
    })
}


// nev bar js 

