// dropdown for the 'My Account' button at the top of the page
$(document).ready(function(){
  $('#my-account').mouseenter(function(){
    var submenu = $('#my-account-options');
    console.log(submenu);

    submenu.css({
      position: "absolute",
      top: $(this).offset().top + $(this).height() + 'px',
      left: $(this).offset().left + 'px',
      zIndex: 1000
    });

    submenu.stop().slideDown(300);

    submenu.mouseleave(function(){
      $(this).slideup(300);
    });
  });
});

// Hamburger menu on the top left, using the Marketo Ball


$(document).ready(function(){
  $('#marketo-ball').click(function(){

    $('.content-container').css('min-height', $(window).height());

    $('nav').css("opacity", 1);

    var contentWidth = $('.container').width();

    $('.content-container').css("width", contentWidth);

    $('#content-layer').css("display", "block");

    $("#container").animate({"marginLeft": ["50%", 'easeOutExpo']}, {
            duration: 700
        });
  });

$('#content-layer').click(function(){

  });

});




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



