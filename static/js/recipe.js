(function () {
  var recipeReady = function() {
		window['dot-widget']({
			lazy: false,
			listItems: $('.ingredient'),
			rightMargin: 41
		});/*
    $('#ingredient-list').width($('#content').width() - $('#content DIV.big-image-container').width());
    $('.ingredient').each(function() {
      var listItem = $(this);
      listItem.find('.list-dots').text('');
      while (listItem.find('SPAN').map(function() { return $(this).width(); }).get().reduce(function(a,b) { return a + b; }) < ($('#ingredient-list').width() - 41)) {
        listItem.find('.list-dots').text(listItem.find('.list-dots').text() + '.');
      }
    });*/
  };

  $(document).ready(recipeReady);
  $(window).resize(recipeReady);
})();
