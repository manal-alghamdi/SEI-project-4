$(document).ready(function() {
    $(function () {
        $(document).scroll(function () {
          var $nav = $(".navbar-fixed-top");
          $nav.css("background-color" , "transparent")
          $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
        });
      });
});



