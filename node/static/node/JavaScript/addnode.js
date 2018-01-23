/**
 * Created by lenovo on 2018/1/23.
 */
$(document).ready(function () {
            $("#nodetype").blur(function () {
                var nodetype = document.getElementById("nodetype").value;
                $("#parentnode").empty();
                if ($.trim(nodetype) == 'global') {

                } else {

                    var data = {
                        "category": nodetype

                    };

                    data = JSON.stringify(data);

                    $.ajax({
                        url: '/v1/node/get_father_pk',
                        type: 'post',
                        dataType: 'json',
                        data: data,

                        success: succFunction,
                        error: erryFunction//成功执行方法    
                    });


                    function erryFunction() {
                        alert("error");
                    }

                    function succFunction(result) {

                        var json = eval(result);

                        for (h = 0; h < json.length; h++) {
                            //循环获取数据    

                            //alert( json[h]['father_pk']);
                            var parentnode = json[h]['father_pk']; //修改parentnode的值
                           // alert(parentnode);
                            $("#parentnode").append($('<option value="' + parentnode + '">' + parentnode + '</option>'));

                        }
                        ;


                    }
                }
            });

        });
        function add_node() {
            var j = 0;

            var nodename = document.getElementById("nodename").value;
            var nodetype = document.getElementById("nodetype").value;//直接获取value中的值
            var parentnode = document.getElementById("parentnode").value;
            var ip = document.getElementById("ip").value;
            var loginnumber = document.getElementById("loginnumber").value;
            var loginpassword = document.getElementById("loginpassword").value;
            var configfilepath = document.getElementById("configfilepath").value;
            var warningfilepath = document.getElementById("warningfilepath").value;
            var alertconfigfilepath = document.getElementById("alertconfigfilepath").value;

            var reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/
            if (loginnumber.length >= 4 && loginnumber.length <= 20 && loginpassword.length >= 6 && loginpassword.length <= 20) {
                j = 1;
            } else {
                alert("账号和密码需4-20位");
            }

            if (reg.test(ip) && j == 1) {
                var data = {
                    "name": nodename,
                    "category": $.trim(nodetype),
                    "father_pk": parentnode,
                    "ip": ip,
                    "username": loginnumber,
                    "password": loginpassword,
                    "prometheus_file": configfilepath,
                    "alert_rule": warningfilepath,
                    "alert_file": alertconfigfilepath
                };

                data = JSON.stringify(data);

                $.ajax({
                    url: '/v1/node/',
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
                alert("IP格式不对");
            }
        }//Node。html中需定义一个路径跳转至该页面