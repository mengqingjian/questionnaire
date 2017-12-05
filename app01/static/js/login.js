/**
 * Created by Administrator on 2017/12/4/004.
 */


$("#subBtn").click(function () {
    $.ajax({
        url:"/login/",
        type:"post",
        data:{
            "username":$("#username").val(),
            "password":$("#password").val(),
            "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val()
        },
        success:function (data) {
            var response = JSON.parse(data);
            console.log(data);
            if (response["is_login"])
                location.href = "/index/";
            else {
                $(".error").html(response["error_msg"]).css("color", "red")
            }
        }
    })
})