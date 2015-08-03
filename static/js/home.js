$( document ).ready(function() {  
  $('.main-logo').animate({'top' : '15%'}, 600);
  $('.home-page-option-container').animate({'margin-bottom' : '5%'}, 600);
  var someSessionVariable = '@Session["username"]';
  console.log(someSessionVariable)
});
