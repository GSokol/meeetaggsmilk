(function() {
	var reside_good = function() {
    var goodId = parseInt($('.good-id').text());
		window['dot-widget']({
			lazy: false,
			listItems: $('DIV.dot-widget-parent'),
			rightMargin: 41,
			spanSelector: '.widget-span'
		});

    var price = {
      priceForGood: 0,
      priceForCut: 0,
      updatePrice: function () {
        $('.good-total-price-value').text(this.priceForGood + this.priceForCut);
      },
      updatePriceForGood: function (price) {
        this.priceForGood = price;
        this.updatePrice();
      },
      updatePriceForCut: function (price) {
        this.priceForCut = price;
        this.updatePrice();
      }
    };

		$('.good-total-price').width(
				$('.good-total-price').width() +
				$('.good-total-price').parent().width() - 40 -
				$('.good-total-price').parent().children().
						map(function() { return $(this).width(); }).get().reduce(function(a, b) { return a + b; })
		);
		$("SELECT").change(function() {
			var selectedVolume = parseFloat($('SELECT OPTION:selected').val().replace(',','.'));
      if (maxResides != undefined) {
        $('.js-price').removeClass('active');
        if (selectedVolume <= maxResides)
          $('.js-price.for-reside').addClass('active');
        else
          $('.js-price.for-supply').addClass('active');
      }
			price.updatePriceForGood(
					Math.round(
						selectedVolume * parseFloat($(".js-price.active").text()) * 100
					) / 100.
			);
			if (selectedVolume > 0) {
				$('.add-to-card').removeClass('inactive');
			} else {
				$('.add-to-card').addClass('inactive');
			}
		});
    $('SPAN INPUT.cut').click(function() {
      if ($(this).prop('checked'))
        price.updatePriceForCut(100);
      else
        price.updatePriceForCut(0);
    });

    $('.add-to-card').unbind('click');
		$('.add-to-card').click(function(event) {
		  if ($(this).hasClass('inactive')) return;
      window.order.addItem(new OrderItem(
            goodId,
            parseFloat($('.js-price').text()),
            parseFloat($('SELECT OPTION:selected').val().replace(',','.')),
            $('SPAN INPUT.cut').prop('checked')
      ));
    });

	};

	$(document).ready(reside_good);
	$(window).resize(reside_good);

})();
