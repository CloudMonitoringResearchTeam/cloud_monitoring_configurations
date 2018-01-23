/**
 * Created by lenovo on 2018/1/5.
 */

 function goto() {

            var username = document.getElementById("username");
            var password = document.getElementById("password");

            var data = {
                "username": username.value,
                "password": password.value
            };

            data = JSON.stringify(data);

            $.ajax({
                url: '/v1/user/login',
                type: 'post',
                dataType: 'json',
                data: data,

                success: succFunction,
                error: erryFunction//成功执行方法????
            });


            function erryFunction() {
                alert("error");
            }

            function succFunction(result) {


                var json = eval(result);

                id1 = json.user_id;
                window.localStorage.setItem("id", id1);

               window.location.href = "/v1/node/index";


            }


        }
