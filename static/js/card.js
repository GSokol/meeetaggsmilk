(function() {

  function removeClickHandler(e) {
    var parentEl = $(this).parent();
    var id = parseInt(/[0-9]+/.exec(parentEl.attr('id'))[0]);
    if (parentEl.hasClass('item-row'))
      window.order.removeItem(id);
    else if (parentEl.hasClass('cut-row'))
      window.order.disableCut(id);
  }

  function orderOnChangeHandler(order, event) {
    $.ajax({
      url: '/order/create/',
      dataType: 'JSON',
      type: 'POST',
      data: { order: JSON.stringify(order.toObject()) },
      success: function(data, statusText, jqXHR) {
        var tbody = $('<TBODY>');
        var group, tr, td, good, removeCell, goodNameCell, goodPriceCell,
              goodValueCell, goodTotalCell, goodsCounter;
        for (var groupCounter = 0; groupCounter < data.supplyGroups.length; groupCounter++) {
          group = data.supplyGroups[groupCounter];
          tr = $('<TR>');
          td = $('<TD>');
          td.addClass('supply-group-header');
          td.attr('colspan', '5');
          td.text(group.maxDate);
          td.appendTo(tr);
          tr.appendTo(tbody);
          for (goodsCounter = 0; goodsCounter < group.goods.length; goodsCounter++) {
            good = group.goods[goodsCounter];

            tr = $('<TR>');
            tr.addClass('supply-group-row item-row');
            tr.attr('id', 'order-item-' + good.id);

            removeCell = $('<TD>');
            removeCell.addClass('supply-group-cell item-remove-cell clickable');
            removeCell.click(removeClickHandler);
            removeCell.appendTo(tr);

            goodNameCell = $('<TD>');
            goodNameCell.addClass('supply-group-cell item-name-cell');
            goodNameCell.text(good.name);
            goodNameCell.appendTo(tr);

            goodPriceCell = $('<TD>');
            goodPriceCell.addClass('supply-group-cell item-price-cell');
            goodPriceCell.text(good.price);
            goodPriceCell.appendTo(tr);

            goodValueCell = $('<TD>');
            goodValueCell.addClass('supply-group-cell item-value-cell');
            goodValueCell.text(good.value);
            goodValueCell.appendTo(tr);

            goodTotalCell = $('<TD>');
            goodTotalCell.addClass('supply-group-cell item-total-cell');
            goodTotalCell.text(good.total);
            goodTotalCell.appendTo(tr);

            tr.appendTo(tbody);

            if (good.cut) {
              tr = $('<TR>');
              tr.addClass('supply-group-row cut-row');
              tr.attr('id', 'order-item-' + good.id + '-cut');

              removeCell = $('<TD>');
              removeCell.addClass('supply-group-cell item-remove-cell clickable');
              removeCell.click(removeClickHandler);
              removeCell.appendTo(tr);

              goodNameCell = $('<TD>');
              goodNameCell.addClass('supply-group-cell item-name-cell');
              goodNameCell.text(good.name);
              goodNameCell.appendTo(tr);

              goodPriceCell = $('<TD>');
              goodPriceCell.addClass('supply-group-cell item-price-cell');
              goodPriceCell.text(good.price);
              goodPriceCell.appendTo(tr);

              goodValueCell = $('<TD>');
              goodValueCell.addClass('supply-group-cell item-value-cell');
              goodValueCell.text(good.value);
              goodValueCell.appendTo(tr);

              goodTotalCell = $('<TD>');
              goodTotalCell.addClass('supply-group-cell item-total-cell');
              goodTotalCell.text(good.total);
              goodTotalCell.appendTo(tr);

              tr.appendTo(tbody);
            }
          }
          if (group.delivery) {
            tr = $('<TR>');
            tr.addClass('supply-group-row delivery-row');

            td = $('<TD>');
            td.addClass('supply-group-cell item-name-cell');
            td.attr('colspan', '4');
            td.text('Доставка');
            td.appendTo(tr);

            td = $('<TD>');
            td.addClass('supply-group-cell item-price-cell');
            td.text(data.deliveryPrice);
            td.appendTo(tr);

            tr.appendTo(tbody);
          }
          tr = $('<TR>');
          tr.addClass('total-row');
          
          td = $('<TD>');
          td.addClass('supply-group-cell item-name-cell');
          td.attr('colspan', '4');
          td.text('Итого');
          td. appendTo(tr);

          td = $('<TD>');
          td.addClass('supply-group-cell item-name-price');
          td.text(group.totalPrice);
          td.appendTo(tr);

          tr.appendTo(tbody);

          $('TABLE.card-table TBODY').remove();
          $('TABLE.card-table').append(tbody);
        }
      }
    });
  }

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
    window.order.addOnChangeHandler(orderOnChangeHandler);
    $('.item-remove-cell').click(removeClickHandler);
  });


})();
