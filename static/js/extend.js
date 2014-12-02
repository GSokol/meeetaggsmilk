function extend(Child, Parent) {
  var F = function () {};
  F.prototype = Parent.prototype;
  Child.prototype = new F();
  Child.prototype.constructor = Child;
  Child.superclass = Parent.prototype;
}

function instanceOf(object, constructor) {
  var o=object;

  while (o.__proto__ != null) {
    if (o.__proto__ === constructor.prototype) return true;
    o = o.__proto__;
  }
  return false;
}

