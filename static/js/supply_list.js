(function() {
  $(document).ready(function() {
    var id = 'vertical-menu-item-' + /([0-9]+)\/?$/.exec(document.location.href)[1];
    $('#' + id).addClass('selected-menu-item');
  });
})();
