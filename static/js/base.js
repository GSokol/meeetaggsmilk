(function() {
  var base_ready = function() {
    $('.phone').mask('+7(999) 999-99-99');
    $('#call-order-submit').click(function() {
      var phone = $('#call-order-phone-input').val();
      $.ajax({
        url: '/call_order/',
        dataType: 'JSON',
        type: 'POST',
        data: {phone: phone},
      });
      $('.horizontal-menu-item-callback').removeClass('selected-menu-item');
      $('#call-order-form').css({display: 'none'});
    });
    $('.horizontal-menu-item-callback').click(function() {
      var top = $('#menu').position().top + $('#menu').outerHeight();
      var right = $(document).width() - ($('#menu').position().left + $('#menu').outerWidth());
      $('#call-order-form').css(
        {display: 'block', top: top.toString() + 'px', right: right.toString() + 'px'}
      );
      $('.horizontal-menu-item-callback').addClass('selected-menu-item');
    });
    $('#content').height(Math.max(
      $('#content').height(),
      [0].concat($('#content').children('DIV, H2').
          map(function() {
            return $(this).height() +
		            parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('margin-top'))) +
                parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('margin-bottom'))) +
                parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('border-top-width'))) +
                parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('border-bottom-width'))) +
                parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('padding-top'))) +
                parseFloat(/[0-9]+\.?[0-9]*/.exec($(this).css('padding-bottom')));
          }).get()).reduce(function(a, b) { return a + b; })
    ));
    var minHeight = Math.max($(document).height() - 40, $('#content').height() + $("#header").height() + 30);
    $("#container").css({'min-height': minHeight + 'px'});
    minHeight -= $("#header").height() + 18;
    var marginLeft = $("#left-menu").width() + 18;
    var marginRight = $("#right-menu").width() + 18;
    $(".long-block").css({'min-height': minHeight + 'px'});
    $("#content").css({'margin-right': marginRight + 'px', 'margin-left': marginLeft + 'px'});
    $(".long-block").height($("#content").height());

    $('#card').width(parseFloat(/[0-9]+\.?[0-9]*/.exec($('#logo').css('margin-left'))) - 40);

    if (window.order == undefined) {
      window.order = new OrderData();

      if (!window.order.handle()) {
        window.order.addOnChangeHandler(function(order, event) {
          $('#card SPAN').text(order.getTotal());
          if (order.getTotal() > 0)
            $('#card').addClass('visible');
          else
            $('#card').removeClass('visible');
          createCookie('card', encodeURIComponent(JSON.stringify(order.toObject())), 100);
        });
      }
      
      var cardStr = getCookie('card');
      if (cardStr != '') {
	      var card = JSON.parse(decodeURIComponent(cardStr));
        if (card.length > 0)
	        for (var i = 0; i < card.length; i++)
            window.order.addItem(new OrderItem(
              card[i].id,
              card[i].price,
              card[i].value,
              card[i].total,
              card[i].cut
            ));
      }
    }
  };

  $(document).ready(base_ready);
  $(window).resize(base_ready);
})();

