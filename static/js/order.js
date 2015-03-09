function OrderData() {
  var that = this;
  var data = [];

  var changeHandlers = [];

  function onChange(event) {
    for (var i = 0; i < changeHandlers.length; i++)
      changeHandlers[i](that, event);
  }

  this.getTotal = function() {
    if (data.length == 0)
      return 0;
    else if (data.length == 1)
      return data[0].getTotal();
    return data.reduce(function (a, b) {
      var aVal, bVal;
      if (a instanceof OrderItem)
        aVal = a.getTotal();
      else
        aVal = a;
      if (b instanceof OrderItem)
        bVal = b.getTotal();
      else
        bVal = b;
      return aVal + bVal; });
  };

  /* Handlers control */
  this.addOnChangeHandler = function(handler) { changeHandlers.push(handler); };
  this.flushOnChangeHandler = function() { changeHandlers = []; };

  this.handle = function() {
    return (changeHandlers.length > 0);
  }

  /* Flush */
  this.flush = function() {
    data = [];
    onChange(new OrderEvent());
  };
  
  /* Get collections */
  this.getCollection = function() {
    return {
      products: data,
      total: that.getTotal()
    };
  };

  this.addItem = function(item) {
    var push = true;
    for (var i = 0; i < data.length; i++)
      if (item.getId() == data[i].getId()) {
        data[i] = item;
        push = false;
        break;
      }
    if (push) data.push(item);
    onChange(new OrderEvent());
  };

  this.removeItem = function(id) {
    for (var i = 0; i < data.length; i++)
      if (data[i].getId() == id) {
        data.splice(i, 1);
        break;
      }
    onChange(new OrderEvent());
  };

  this.disableCut = function(id) {
    for (var i = 0; i < data.length; i++)
      if (data[i].getId() == id) {
        data[i].disableCut();
        break;
      }
    onChange(new OrderEvent());
  };

  this.toObject = function () {
    var ret = [];
    for (var i = 0; i < data.length; i++) {
      var obj = data[i];
      ret.push(obj.toObject());
    }
    return ret;
  };
}

function OrderEvent() {
/*  OrderEvent.superclass.constructor.apply(this, Event); */
}
/* extend(OrderEvent, Event); */

function SupplyCollection(data) {
  var that = this;

  data.sort(function(a, b) { a.getDate() > b.getDate() });

  this.products = [];
  this.total = 0;

  for (var i = 0; i < data.length; i++) {
    if (this.products.length == 0 || this.products[this.products.length - 1] != data[i].getDate())
      this.products.push({date: data[i].getDate(), items: [data[i]]});
    else
      this.products[this.products.length - 1].items.push(data[i]);
    this.total += data[i].getTotal();
  }
}

function OrderException() {};
function OrderConsistencyException() {};
extend(OrderConsistencyException, OrderException);

function OrderItem(id, price, value, cut) {
  var _total = price * value;
  var _shownTotal = _total;
  var _cut;
  if (cut == undefined)
    _cut = false;
  else
    _cut = cut;
  if (_cut)
    _shownTotal += 100;

  var _id = id;
  var _price = price;
  var _value = value;

  this.disableCut = function() {
    if (_cut) {
      _shownTotal -= 100;
      _cut = false;
    }
  };


  this.getId = function() { return _id; };
  this.getPrice = function() { return _price; };
  this.getValue = function() { return _value; };
  this.getTotal = function() { return _shownTotal; };
  this.getCut = function() { return _cut; };
  this.toObject = function() {
    return {
      id: _id,
      price: _price,
      value: _value,
      cut: _cut,
      total: _total
    };
  };
}
