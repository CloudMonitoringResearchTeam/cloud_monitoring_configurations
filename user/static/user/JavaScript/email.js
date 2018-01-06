function add_user() {

    var username = document.getElementById("username");
    var password = document.getElementById("password1");
    if (username.value.length == 0) {
        alert("邮箱不能为空");
    }
    else {
       // alert(username.value);
        var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(\.[a-zA-Z0-9_-])+/;


        if (reg.test(username.value)) {
            var data = {
                "username": username.value,
                "password": password.value
            };

            data = JSON.stringify(data);

            $.ajax({
                url: '/v1/user/',
                type: 'post',
                dataType: 'text',
                data: data,

                success: succFunction,
                error: erryFunction//成功执行方法    
            });


            function erryFunction() {
                alert("error");
            }

            function succFunction() {


                alert("success");
                window.location.href = "/v1/node/index";

            }

        } else {
            alert("邮箱格式不正确");
        }

    }
}




