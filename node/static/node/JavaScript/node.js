/**
 * Created by lenovo on 2018/1/23.
 */
 function table() {
            $.ajax({
                url: '/v1/node/',//修改
                type: 'get',
                dataType: 'json',


                success: succFunction,
                error: erryFunction//成功执行方法????
            });


            function erryFunction() {
                alert("error");
            }

            function succFunction(result) {


                var json = eval(result);

                for (j = 0; j < json.length; j++) {//修改

                    $("#tb").append(
                            $('<tr><td><input type="checkbox" name="category"  class="category"  style="display: none" value="' + json[j].pk + '"/></td>' +
                                    '<td id="nodeid' + json[j].pk + '">' + json[j].pk + '</td>' +
                                    '<td>' + json[j]['fields'].name + '</td>' +
                                    '<td>' + json[j]['fields'].category + '</td>' +
                                    '<td>' + json[j]['fields'].father_pk + '</td>' +
                                    '<td>' + json[j]['fields'].ip + '</td>' +
                                    '<td>' + json[j]['fields'].pro_conf_file_path + '</td>' +
                                    '<td>' + json[j]['fields'].pro_alert_rule_path + '</td>' +
                                    '<td>' + json[j]['fields'].alert_conf_file_path + '</td>' +
                                    '<td>' +
                                    '' +
                                    '<button type="button" class="btn  active btn-primary node1" name="' + json[j].pk + '"onclick=delete1(this.name)>删除节点</button>&nbsp;' +
                                    '<button type="button" class="btn  active btn-primary node2" name="' + json[j].pk + '" onclick=config(this.name)>查看配置</button>&nbsp;' +
                                    '<button type="button" class="btn  active btn-primary node3" name="' + json[j].pk + '" onclick=config(this.name)>更新配置</button></td></tr>'));
                   //alert(json[j]['fields'].category);
                    window.localStorage.setItem('category' + json[j].pk , json[j]['fields'].category);
                   // alert('category ' + json[j].pk);
                    //alert(window.localStorage.getItem('category ' + json[j].pk));


                }
            }


        }
        ;


        function delete1(name) {//删除节点


            var data = "["
            data += ' {"node_id":"' + name + '" }]';
            alert(data);
            $.ajax({
                url: '/v1/node/',
                type: 'delete',
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
        ;

        function config(name) {  //查看配置，更改配置
            //删除节点
            //?$(this)表示获取当前被点击元素的name值
            //alert(value);
            var type = window.localStorage.getItem('category' + name );
            //alert('category'+name);
            //alert(type);
            if (type == "work") { //修改
                alert("工作节点没有配置");
            } else {


                if (type == "global") {
                    window.location.href = "/v1/global"; //修改到全局页面
                }
                if (type == "cluster") {
                    window.location.href = "/v1/cluster";//修改到集群页面
                }

                // alert("success");


            }

            ;
        }
        function newnode() {
            window.location.href = "add_node_view";
        }

        var l = 0;

        function deletall() {//未写完

            if (l == 0) {
                $(".category").show();
                l = 1;
            }
            else {
                var check = document.getElementsByName("category");
                var len = check.length;
                var checked = 0;


                var data = "[";
                for (var i = 0; i < len; i++) {
                    if (check[i].checked) {
                        data += ' {"node_id":"' + check[i].value + '" },';

                        checked++;
                    }
                }
                //去掉最后一个","
                var reg = /,$/gi;
                data = data.replace(reg, "");
                data += "]";
                if (checked == 0) {
                    alert("未选择");

                }
                else {
                    alert(data);
                    //data = JSON.stringify(data);
                    // alert(data);
                    $.ajax({
                        url: '/v1/node/',
                        type: 'delete',
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

                $(".category").hide();
                if ($(this).is(":checked")) {
                    $("[name='category']:checkbox").prop("checked", true);
                } else {
                    $("[name='category']:checkbox").prop("checked", false);
                }
                l = 0;
            }


        }
        ;

        function shown() {


            $.ajax({
                url: '/v1/node/get_all_nodes',//修改
                type: 'post',//修改
                dataType: 'json',


                success: succFunction,
                error: erryFunction
            });
            function erryFunction() {
                alert("error");
            }

            function succFunction(result) {

                $("#global").text(result['global']);
                $("#cluster").text(result['cluster']);
                $("#work").text(result['work']);
                // $("#global").text(json[0]);


            }


        }
