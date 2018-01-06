/**
 * Created by lenovo on 2018/1/3.
 */
i=0;
$(document).ready(function(){

    $(".selfcenter").click(function(){
             if(i==0)
             {
                 $(".admin,.serect").show();

                 i=1;
             }else{
                 $(".admin,.serect").hide();

                 i=0;
             }

            });




        });

