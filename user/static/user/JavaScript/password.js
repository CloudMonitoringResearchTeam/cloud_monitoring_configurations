/**
 * Created by lenovo on 2017/12/29.
 */


    function goto() {

        i = 0;
        var password = $("#inputPassword2").val();
        var password2 = $("#inputPassword3").val();
        if (password.length <6 || password2.length <6) {
            alert("密码不能少于6位");
        } else {
            if (password == password2) {
                if (/[a-z]+/.test(password)) {
                    i = i + 1;
                }
                if (/[A-Z]+/.test(password)) {
                    i = i + 1;
                }
                if (/[0-9]+/.test(password)) {
                    i = i + 1;
                }
                if (/\W+\D+/.test(password)) {
                    i = i + 1;

                }
                if (i < 2) {
                    alert("密码至少包含大小写字母，数字，特殊字符，其中的两种");
                } else {

                    var id = window.localStorage.getItem("id");

                    //alert(typeof (id));
                    var password3 = document.getElementById("inputPassword3");
                    //alert(password3.value);
                    var data = {
                        "password": password3.value,
                        "user_id": id
                    };

                    data = JSON.stringify(data);

                    $.ajax({
                        url: '/v1/user/password',
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
                }

            }
            else{
                alert("确认密码于新密码不一致");
            }
        } }



