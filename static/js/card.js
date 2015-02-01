(function() {
  $(document).ready(function() {
    $('input:submit').click(function (e) {
      e.preventDefault();
      e.stopPropagation();
      var input = document.createElement('input');
      input.type = 'hidden';
      input.name = 'order';
      input.value = JSON.stringify(window.order.toObject());
      this.form.appendChild(input);
      this.form.submit();
    });
  });
})();
