$(document).ready(function(){
  //$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
  $("#login-submit").click(function( event ) {
    var loginCreds = {
      username : $('#username').val(),
      password : $('#password').val()
    }
    $.ajax({
        type: 'POST',
        url: 'creds',
        data: JSON.stringify(loginCreds),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    })
    .done(function(msg) {
      console.log("success");
      if(msg.resp == "fail"){
        $('#login-message').css('display','block');
      }
      else{
        window.location = "/";
      }
    })
    .fail(function() {
      console.log("error");
    })
    .always(function() {
      console.log("complete");
    });
  });
})