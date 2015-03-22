(function() {
  $(document).ready(function() {
    var 
    $("#owl-demo").owlCarousel({
      items: Math.floor($('#owl-demo').parent().width() / $('#owl-demo .bordered-block').outerWidth()),
      navigation: false,
      slideSpeed: 300,
      paginationSpeed: 400,
      autoPlay: 3000
    });
  });
})();
