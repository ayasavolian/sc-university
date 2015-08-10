// this is how we do the FAQ question/answer dropdown
$(document).ready(function(){

  $('div.dropdown').each(function() {
    var $dropdown = $(this);

    $($dropdown).click(function(e) {
      e.preventDefault();
      $div = $("div.dropdown-container", $dropdown);
      $div.toggle();
      $("div.dropdown-container").not($div).hide();
      return false;
    });

});
    
  $('html').click(function(){
    $("div.dropdown-container").hide();
  });
     
});

// Dynamic content swap images and text

$('#headshot-1').click(function(){
      $('.dc-right-container').attr("src", "../assets/img/dc-ny.jpg").toggle();
      $('#dc-invite').attr("src", "../assets/img/dc-lucy.png").toggle();
  });

$('#headshot-2').click(function(){
      $('.dc-right-container').attr("src", "../assets/img/dc-sf.jpg").toggle();
      $('#dc-invite').attr("src", "../assets/img/dc-joey.png").toggle();
  });

$('#headshot-3').click(function(){
      $('.dc-right-container').attr("src", "../assets/img/dc-chi.jpeg").toggle();
      $('#dc-invite').attr("src", "../assets/img/dc-jamey.png").toggle();
  });



