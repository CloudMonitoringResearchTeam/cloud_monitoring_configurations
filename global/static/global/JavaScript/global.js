/**
 * Created by lenovo on 2018/1/23.
 */
/**
 * Created by lenovo on 2018/1/23.
 */
 $(document).ready(function () {

            $("#updatebutton1").click(function () {
                // alert("hello");
                $("#textarea1").empty();
                $("#textarea2").empty();
                var filetype = document.getElementById("filetype").value;

                var data = {

                    "filetype": filetype  //修改
                };

                data = JSON.stringify(data);
                var url = '/v1/global/conf_file?file_type=' + filetype;

                $.get({   //将ajax改成了get
                    url: url,//修改
                    // type: 'POST',
                    dataType: 'text',


                    success: succFunction,
                    error: erryFunction//成功执行方法????
                });


                function erryFunction() {
                    //alert(filetype.value);
                    alert("未更新");
                }

                function succFunction(result) {

                   // alert(result);

                    $("#textarea1").text(result);


                    $("#textarea2").text(result);
                }


            });
            })
              function update() {


            var text2 = document.getElementById("textarea2");


            var file = document.getElementById("filetype");
            var data = {

                "filetype": filetype.value,
                "conf_file": text2.value//修改

            };
            data = JSON.stringify(data);

            $.ajax({
                url: '/v1/global/conf_file',//修改
                type: 'POST',
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
                 // $("#textarea1").empty();
                  //$("#textarea2").empty();
                 window.location.reload();

            }

        }
        ;


