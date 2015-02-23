(function($) {

  var remarkColoredList = function(target) {
    $(target).each(function(index) {
      var el = $(this);
      el.removeClass('row1 row2');
      if ((index % 2) == 0)
        el.addClass('row1');
      else
        el.addClass('row2');
    });
  };

  var makeListSortable = function() {
    $('TABLE#result_list TBODY').sortable({
      axis: 'y',
      update: function(event, ui) {
        remarkColoredList(this.children);
        var elementId = $(ui.item[0].children[0].children[0]).val();
        var beforeId = undefined;
        $($(ui.item[0]).parent().children()).each(function() {
          if (this == ui.item[0])
            return false;
          beforeId = $(this.children[0].children[0]).val();
        });

        url = '/supply/change_order/' + elementId + '/';
        if (beforeId == undefined)
          url += '/';
        else
          url += beforeId + '/';
        jQuery.ajax({
          url: url,
          error: function(data, statusText, jqXHR) {
            alert(statusText + JSON.stringify(data));
          }
        }); 
      }
    });
  };

  var Row = function (row) {
    
    var that = this;
    var id = $(row.children[0].children[0]).val();
    var name = row.children[1].children[0].innerText;
    var hidden = $(row.children[2].children[0]).attr('alt') == 'True';
    var after = row.children[3].innerText;
    if (after == '(Ничего)')
      after = undefined;

    this.getId = function() {
      return id;
    };

    this.getName = function() {
      return name;
    };

    this.isHidden = function() {
      return hidden;
    };

    this.getAfter = function() {
      return after;
    };

    this.getIdColumn = function() {
      return row.children[0];
    };

    this.getNameColumn = function() {
      return row.children[1];
    };

    this.getHiddenColumn = function() {
      return row.children[2];
    };

    this.getAfterColumn = function() {
      return row.childrem[3];
    };

    this.getEl = function() {
      return row;
    };
  };

  var sortListByRealOrder = function() {
    var rows = {};
    $('TABLE#result_list TBODY TR').each(function() {
      var row = new Row(this);
      rows[row.getAfter()] = row;
    });
    sortedRows = [rows[undefined]];
    delete rows[undefined];
    while (Object.keys(rows).length != 0) {
      sortedRows.push(rows[sortedRows[sortedRows.length - 1].getName()]);
      delete rows[sortedRows[sortedRows.length - 1].getAfter()];
    }

    var tbody = $('TABLE#result_list TBODY');
    tbody.html('');
    for (var i = 0; i < sortedRows.length; i++) {
      tbody.append(sortedRows[i].getEl());
    }
  };

  $(document).ready(function () {
    $('TABLE#result_list THEAD .column-after').css({display:'none'});
    $('TABLE#result_list TBODY .field-after').css({display:'none'});
    sortListByRealOrder();
    remarkColoredList($('TABLE#result_list TBODY').children());
    makeListSortable();
  });
})(jQuery);
