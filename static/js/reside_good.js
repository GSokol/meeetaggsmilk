(function() {
	var reside_good = function() {
		window['dot-widget']({
			lazy: false,
			listItems: $('DIV.dot-widget-parent'),
			rightMargin: 41,
			spanSelector: '.widget-span'
		});

		$('.good-total-price').width(
				$('.good-total-price').width() +
				$('.good-total-price').parent().width() - 40 -
				$('.good-total-price').parent().children().
						map(function() { return $(this).width(); }).get().reduce(function(a, b) { return a + b; })
		);
		$("SELECT").change(function() {
			var selectedVolume = parseFloat($('SELECT OPTION:selected').val());
			$('.good-total-price-value').text(
					Math.round(
						selectedVolume * parseFloat($(".js-price").text()) * 100
					) / 100
			);
			if (selectedVolume > 0) {
				$('.add-to-card').removeClass('inactive');
			} else {
				$('.add-to-card').addClass('inactive');
			}
		});

    $('.add-to-card').unbind('click');
		$('.add-to-card').click(function(event) {
		  if ($(this).hasClass('inactive')) return;
      window.order.addOrderItem(new ResideOrderItem(
            /([0-9]+)\/?$/.exec(document.location.href)[1],
            $('H2').first().text(),
            parseFloat($('.js-price').text()),
            parseFloat($('SELECT OPTION:selected').val()),
            parseFloat($('.good-total-price-value').text())
      ));
    });

	};

	$(document).ready(reside_good);
	$(window).resize(reside_good);

})();
