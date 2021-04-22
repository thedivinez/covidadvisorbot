var me = {};
var ipaddress = "";
me.avatar = "../static/images/me.jpg";
$.getJSON('https://api.ipify.org?format=jsonp&callback=?', function (data) {
  ipaddress = data.ip;
});
var you = {};
you.avatar = "../static/images/you.png";

function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0' + minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time) {
  if (time === undefined) {
    time = 0;
  }
  var control = "";
  var date = formatAMPM(new Date());

  if (who == "me") {
    control = '<li style="width:100%">' +
      '<div class="msj macro">' +
      '<div class="avatar"><img class="img-circle" style="width:100%;" src="' + me.avatar + '" /></div>' +
      '<div class="text text-l">' +
      '<p>' + text + '</p>' +
      '<p><small>' + date + '</small></p>' +
      '</div>' +
      '</div>' +
      '</li>';
  } else {
    control = '<li style="width:100%;">' +
      '<div class="msj-rta macro">' +
      '<div class="text text-r">' +
      '<p>' + text + '</p>' +
      '<p><small>' + date + '</small></p>' +
      '</div>' +
      '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%;" src="' + you.avatar + '" /></div>' +
      '</li>';
  }
  setTimeout(
    function () {
      $("ul").append(control).scrollTop($("ul").prop('scrollHeight'));
    }, time);

}

function resetChat() {
  $("ul").empty();
}

$(".mytext").on("keydown", function (e) {
  if (e.which == 13) {
    var text = $(this).val();
    if (text !== "") {
      insertChat("you", text);
      $(this).val('');
      setTimeout(
        function () {
          $.get(`${window.location.origin}/newmessage?message=${text}&ip_address=${ipaddress}`, function (data, status) {
            insertChat("me", data.message);
          });
        }, 2000);

    }
  }
});

$('body > div > div > div:nth-child(2) > span').click(function () {
  $(".mytext").trigger({ type: 'keydown', which: 13, keyCode: 13 });
})

//-- Clear Chat
resetChat();