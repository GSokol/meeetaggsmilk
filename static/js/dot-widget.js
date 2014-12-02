(function() {
	window['dot-widget'] = function (config) {
		if (config.spanSelector == undefined)
			config.spanselector = 'SPAN';
		this.execute = function() {
			config.listItems.each(function() {
				var listItem = $(this);
				listItem.find('.dot-widget-center').text('');
				while (listItem.find('SPAN').map(function() { return $(this).width(); }).get().reduce(function(a,b) { return a + b; }) < ($('.dot-widget-parent').width() - config.rightMargin)) {
					listItem.find('.dot-widget-center').text(listItem.find('.dot-widget-center').text() + '.');
				}
			});
		};
		if (config.lazy) {
		$(document).ready(this.execute);
		$(window).resize(this.execute);
		} else {
			this.execute();
		}
	};
})();
