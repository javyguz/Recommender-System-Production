var data = JSON.parse(document.getElementById('Recommendation').textContent);
var first = JSON.parse(document.getElementById('First').textContent);
var data1 = JSON.parse(document.getElementById('data').textContent);
var mylist = JSON.parse("{{mylistjson}}")
console.log(mylist)
console.log(data1)


if (data.length == 0 && first == "false"){
    const errorMessage = document.createTextNode("El libro no existe en la base de datos");
    document.getElementById("images").appendChild(errorMessage);
    console.log(errorMessage);
}
else{
    for (i in data){

        var img = document.createElement('img');
        src = data[i];
        img.src = src;
        img.setAttribute("height", "250");
        img.setAttribute("width", "200");
        img.class = "img-thumbnail";

        document.getElementById("images").appendChild(img);
    }
}

var search_terms = {{data | safe}};

function autocompleteMatch(input) {
  if (input == '') {
    return [];
  }
  var reg = new RegExp(input)
  return search_terms.filter(function(term) {
      if (term.match(reg)) {
      return term;
      }
  });
}

function showResults(val) {
  res = document.getElementById("result");
  res.innerHTML = '';
  let list = '';
  let terms = autocompleteMatch(val);
  for (i=0; i<terms.length; i++) {
    list += '<option>' + terms[i] + '</option>';
  }
  res.innerHTML = '<select onchange="changeFunc(value);" id="ddlViewBy">' + list + '</select>';

}

function changeFunc(i) {
    document.getElementById("mytextbox").value = i;
}
