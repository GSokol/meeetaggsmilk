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
    return data.reduce(function (a, b) { return a.getTotal() + b.getTotal(); });
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
  }

  this.toObject = function () {
    var ret = [];
    for (var i = 0; i < data.length; i++) {
      var obj = data[i];
      ret.push({
        id: obj.getId(),
        name: obj.getName(),
        price: obj.getPrice(),
        value: obj.getValue(),
        total: obj.getTotal(),
        cut: obj.getCut(),
      });
    }
    return ret;
  };
}

function OrderEvent() {}

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

function OrderItem(id, name, price, value, total, cut) {
  var _total = price * value;
  if (_total > total || total < total)
    throw new OrderConsistencyException();

  var _id = id;
  var _name = name;
  var _price = price;
  var _value = value;
  var _cut = cut;


  this.getId = function() { return _id; };
  this.getName = function() { return _name; };
  this.getPrice = function() { return _price; };
  this.getValue = function() { return _value; };
  this.getTotal = function() { return _total; };
  this.getCut = function() { return _cut; };
}
