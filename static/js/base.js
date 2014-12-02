(function() {
  var base_ready = function() {
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
      
      var cardStr = encodeURIComponent(getCookie('card'));
      if (cardStr != '') {
	      var card = JSON.parse(cardStr);
	      for (var i = 0; i < card[window.order.RESIDE].length; i++)
          window.order.addOrderItem(new ResideOrderItem(
            card[window.order.RESIDE][i].id,
            card[window.order.RESIDE][i].name,
            card[window.order.RESIDE][i].price,
            card[window.order.RESIDE][i].value,
            card[window.order.RESIDE][i].total
          ));
	      for (var i = 0; i < card[window.order.SUPPLY].length; i++)
          window.order.addOrderItem(new SupplyOrderItem(
            card[window.order.SUPPLY][i].id,
            card[window.order.SUPPLY][i].name,
            card[window.order.SUPPLY][i].price,
            card[window.order.SUPPLY][i].value,
            card[window.order.SUPPLY][i].total,
            (new Date(card[window.order.SUPPLY][i].date))
          ));
      }
    }
    if (!window.order.handle()) {
      window.order.addOnChangeHandler(function(order, event) {
        $('#card SPAN').text(order.getTotal());
        if (order.getTotal() > 0)
          $('#card').addClass('visible');
        else
          $('#card').removeClass('visible');
        setCookie('card', encodeURIComponent(JSON.stringify(order.toObject())), 100);
      });
    }
  };

  $(document).ready(base_ready);
  $(window).resize(base_ready);
})();

