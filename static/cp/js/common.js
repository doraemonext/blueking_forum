define(['jquery', 'bootstrap', 'noty'], function ($) {
    // 设置CSRF
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.noty.defaults = {
        layout: 'bottomCenter',
        theme: 'defaultTheme',
        type: 'alert',
        text: '', // can be html or string
        dismissQueue: true, // If you want to use queue feature set this true
        template: '<div class="noty_message"><span class="noty_text"></span><div class="noty_close"></div></div>',
        animation: {
            open: {height: 'toggle'},
            close: {height: 'toggle'},
            easing: 'swing',
            speed: 600 // opening & closing animation speed
        },
        timeout: 3000, // delay for closing event. Set false for sticky notifications
        force: false, // adds notification to the beginning of queue when set to true
        modal: false,
        maxVisible: 5, // you can set max visible notification for dismissQueue true option,
        killer: false, // for close all notifications before show
        closeWith: ['click'], // ['click', 'button', 'hover']
        callback: {
            onShow: function () {
            },
            afterShow: function () {
            },
            onClose: function () {
            },
            afterClose: function () {
            }
        },
        buttons: false // an array of buttons
    };
});