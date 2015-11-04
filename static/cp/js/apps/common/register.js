define(function(require, exports, module) {
    require('common');
    require('jquery-validate');
    var $ = require('jquery');

    $("#register-form").validate({
        rules: {
            username: "required",
            email: {
                required: true,
                email: true
            },
            password: "required",
            password_confirm: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            username: {
                required: "用户名不能为空"
            },
            email: {
                required: "用户名不能为空",
                email: "请输入合法的 Email 地址"
            },
            password: {
                required: "密码不能为空"
            },
            password_confirm: {
                required: "确认密码不能为空",
                equalTo: "两次密码输入不一致"
            }
        },
        highlight: function(element) {
            $(element).parent().addClass("has-error");
        },
        unhighlight: function(element) {
            $(element).parent().removeClass("has-error");
        },
        submitHandler: function(form) {
            var validator = this;

            $.ajax({
                type: "POST",
                dataType: "json",
                url: "/api/common/register/",
                cache: false,
                data: {
                    username: $("input[name=username]").val(),
                    email: $("input[name=email]").val(),
                    password: $("input[name=password]").val(),
                    next: $("input[name=next]").val()
                },
                beforeSend: function() {
                    $("button[type=submit]").attr("disabled", "disabled");
                    $("button[type=submit]").text("注册中…");
                },
                success: function(data) {
                    window.location.href = data["redirect_url"];
                },
                statusCode: {
                    400: function(xhr) {
                        var data = $.parseJSON(xhr.responseText);
                        var errors = {};
                        for (var key in data) {
                            if (key == "non_field_errors") {
                                errors["password"] = data[key][0];
                            } else {
                                errors[key] = data[key][0];
                            }
                        }
                        validator.showErrors(errors);
                    }
                },
                complete: function() {
                    $("button[type=submit]").removeAttr("disabled");
                    $("button[type=submit]").text("注册");
                }
            });
            return false;
        }
    });
});
