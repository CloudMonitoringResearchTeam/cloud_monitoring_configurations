/**
 * Created by lenovo on 2018/1/23.
 */
 $(document).ready(function () {
            var text = localStorage.getItem("config");
            var reg = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/
            $("#updatebutton1").click(function () {
                $("#textarea1").empty();
                $("#textarea2").empty();

                var ip = document.getElementById("ip").value;
                var filetype = document.getElementById("filetype").value;

               // var data = {
                   // "ip": ip,//修改
                   // "filetype": filetype
               // };

               //data = JSON.stringify(data);
                if (reg.test(ip)) {
                    $.get({
                        url: '/v1/cluster/conf_file?file_type=' + filetype + '&ip=' + ip,
                        // type: 'post',
                        dataType: 'text',
                        //data: data,

                        success: succFunction,
                        error: erryFunction//成功执行方法????
                    });


                    function erryFunction() {
                        alert("error");
                    }

                    function succFunction(result) {



                        $("#textarea1").text(result);
                        $("#textarea2").text(result);

                    }

                } else {
                    var clear=document.getElementById("ip");
                    clear.value=" ";
                    alert("IP格式不对");

                }
            });
        })
        function update() {
            //alert("hello");
            var ip = document.getElementById("ip");
            var filetype = document.getElementById("filetype");
            var text2 = document.getElementById("textarea2");
            var data = {
                "ip": ip.value,//修改
                "filetype": filetype.value,
                "conf_file": text2.value//修改

            };

            data = JSON.stringify(data);

            $.ajax({
                url: '/v1/cluster/conf_file',
                type: 'post',
                dataType: 'text',
                data: data,

                success: succFunction,
                error: erryFunction//成功执行方法????
            });


            function erryFunction() {
                alert("error");
            }

            function succFunction() {

                alert("success");
                window.location.reload();

            }
        }
