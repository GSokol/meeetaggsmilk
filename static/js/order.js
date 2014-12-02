function OrderData() {
  var that = this;
  this.RESIDE = 'reside';
  this.SUPPLY = 'supply';
  var data = {};
  data[that.RESIDE] = [];
  data[that.SUPPLY] = [];

  var changeHandlers = [];
  var resideChangeHandlers = [];
  var supplyChangeHandlers = [];

  function onChange(event) {
    for (var i = 0; i < changeHandlers.length; i++)
      changeHandlers[i](that, event);
  }

  function onCustomChange(event, handlers) {
    onChange(event);
    for (var i = 0; i < handlers.length; i++)
      handlers[i](that, event);
  }

  function onResideChange(event) {
    onCustomChange(event, resideChangeHandlers);
  }

  function onSupplyChange(event) {
    onCustomChange(event, supplyChangeHandlers);
  }

  function _getTotal(totalType) {
    if (data[totalType].length == 0)
      return 0;
    else if (data[totalType].length == 1)
      return data[totalType][0].getTotal();
    return data[totalType].reduce(function (a, b) { return a.getTotal() + b.getTotal(); });
  }

  /* Get total prices */
  this.getResideTotal = function() {
	  return _getTotal(that.RESIDE); 
  };
  this.getSupplyTotal = function() { return _getTotal(that.SUPPLY); };
  this.getTotal = function() { return that.getResideTotal() + that.getSupplyTotal(); };

  /* Handlers control */
  this.addOnChangeHandler = function(handler) { changeHandlers.push(handler); };
  this.flushOnChangeHandler = function() { changeHandlers = []; };

  this.addOnResideChangeHandler = function(handler) { resideChangeHandlers.push(handler); };
  this.flushOnResideChangeHandler = function() { resideChangeHandlers = []; };

  this.addOnSupplyChangeHandler = function(handler) { supplyChangeHandlers.push(handler); };
  this.flushOnResideChangeHandler = function() { supplyChangeHandlers = []; };

  this.handle = function() {
    return (changeHandlers.length > 0) ||
	    (resideChangeHandlers. length > 0) || (supplyChangeHandlers.length > 0);
  }

  /* Flush */
  this.flushResides = function() {
    data[that.RESIDE] = [];
    onResideChange(new OrderEvent());
  };
  this.flushSupplies = function() {
    data[that.SUPPLY] = [];
    onSupplyChange(new OrderEvent());
  };
  
  /* Get collections */
  this.getResideCollection = function() {
    return {
      products: data[that.RESIDE],
      total: that.getResideTotal()
    };
  };

  this.getSupplyCollection = function() {
    return new SupplyCollection(data[thst.SUPPLY]);
  };

  function addItem(item, itemType) {
    var push = true;
    for (var i = 0; i < data[itemType].length; i++)
      if (item.getId() == data[itemType][i].getId()) {
        data[itemType][i] = item;
        push = false;
      }
    if (push) data[itemType].push(item);
  }


  function addReside (resideItem) {
    addItem(resideItem, that.RESIDE);
    onResideChange(new OrderEvent());
  }

  function addSupply (supplyItem) {
    addItem(supplyItem, that.SUPPLY);
    onSupplyChange(new OrderEvent());
  }

  this.addOrderItem = function (orderItem) {
    if (instanceOf(orderItem, SupplyCollection))
      addSupply(orderItem);
    else if (instanceOf(orderItem, ResideOrderItem))
      addReside(orderItem);
    else
      throw new OrderTypeException();
  };

  this.toObject = function () {
    var ret = {};
    ret[that.SUPPLY] = [];
    for (var i = 0; i < date[that.SUPPLY].length; i++) {
      var obj = date[that.SUPPLY][i];
      ret[that.SUPPLY].push({
        id: obj.getId(),
        name: obj.getName(),
        price: obj.getPrice(),
        value: obj.getValue(),
        total: obj.getTotal(),
        date: obj.getDate().valueOf()
      });
    }
    ret[that.RESIDE] = [];
    for (var i = 0; i < date[that.RESIDE].length; i++) {
      var obj = date[that.RESIDE][i];
      ret[that.RESIDE].push({
        id: obj.geId(),
        name: obj.getName(),
        price: obj.getPrice(),
        value: obj.getValue(),
        total: obj.getTotal()
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
function OrderTypeException() {};
extend(OrderTypeException, OrderException);

function OrderItem(id, name, price, value, total) {
  var _total = price * value;
  if (_total > total || total < total)
    throw new OrderConsistencyException();

  var _id = id;
  var _name = name;
  var _price = price;
  var _value = value;


  this.getId = function() { return _id; };
  this.getName = function() { return _name; };
  this.getPrice = function() { return _price; };
  this.getValue = function() { return _value; };
  this.getTotal = function() { return _total; };
}

function ResideOrderItem(id, name, price, value, total) {
  ResideOrderItem.superclass.constructor.call(this, id, name, price, value, total);
}
extend(ResideOrderItem, OrderItem);

function SupplyOrderItem(id, name, price, value, total, date) {
  SupplyOrderItem.superclass.constructor.call(this, id, name, price, value, total);
  var _date = date;
  this.getDate = function() { return _date; };
}
extend(SupplyOrderItem, OrderItem);
