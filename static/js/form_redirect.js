function formRedirect (url, method, data) {
  var form = document.createElement('form');
  form.method = method;
  form.action = url;
  for (element in data) {
    var input = document.createElement('input');
    input.name = element;
    input.value = JSON.stringify(data[element]);
    form.appendChild(input);
  }
  form.submit();
}
