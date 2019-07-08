let quotes = [];
let bad_quotes = [];
let good_quotes = [];

function render_main_quote() {
  $("#quote").text(quotes[0]);
}

function render_good_quotes() {
  $("#good-list").empty();
  for (let i = 0; i < good_quotes.length; i++) {
    $("#good-list").append("<a onclick=\"move_good_quote(" + i + ")\" class=\"list-group-item list-group-item-action\">" + good_quotes[i] + "</a>");
  }
}

function render_bad_quotes() {
  $("#bad-list").empty();
  for (let i = 0; i < bad_quotes.length; i++) {
    $("#bad-list").append("<a onclick=\"move_bad_quote(" + i + ")\" class=\"list-group-item list-group-item-action\">" + bad_quotes[i] + "</a>");
  }
}

function render_quotes() {
  render_main_quote();
  render_good_quotes();
  render_bad_quotes();
}

function add_quote(q) {
  quotes.unshift(q);
}

function add_quotes(q) {
  for (let i = 0; i < q.length; i++) add_quote(q[i]);
}

function move_good_quote(i) {
  add_quotes(good_quotes.splice(i, 1));
  render_quotes();
}

function move_bad_quote(i) {
  add_quotes(bad_quotes.splice(i, 1));
  render_quotes();
}

function load_new_quotes() {
  if (quotes.length <= 1) {
    $.ajax({
      url: "api?n=10",
      success: function(result) {
        add_quotes(result.quotes);
        render_quotes();
      }
    });
  } else {
    render_quotes();
  }
}

function add_default_quote() {
  if (quotes.length == 0) add_quote($("#quote").text());
}

$("#good-button").click(function() {
  add_default_quote();

  // Move first quote from quotes to good_quotes
  good_quotes.unshift(quotes.shift());

  load_new_quotes();
});

$("#bad-button").click(function() {
  add_default_quote();

  // Move first from quotes to bad_quotes
  bad_quotes.unshift(quotes.shift());

  load_new_quotes();
});

$("#copy").click(function() {
  let $temp = $("<input>");
  $("body").append($temp);
  $temp.val($("#quote").text()).select();
  document.execCommand("copy");
  $temp.remove();
});

$("#download").click(function() {
  let content = "data:text/csv;charset=utf-8,";

  for (let i = 0; i < good_quotes.length; i++) {
    content += good_quotes[i] + "\r\n";
  }

  var uri = encodeURI(content);
  var link = document.createElement("a");
  link.setAttribute("href", uri);
  link.setAttribute("download", "hackerquotes.txt");
  document.body.appendChild(link);

  link.click();
});