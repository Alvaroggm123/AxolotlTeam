$(document).ready(function () {
  var chatBtn = document.getElementById("chatBtn");
  var chat = document.getElementById("chat");
  chat.style.display = "none";
  chatBtn.addEventListener("click", function () {
    var display = chat.style.display;
    console.log(display);
    // if (display == "none") {
    //   chat.style.display = "block";
      
    // } else {
    //   chat.style.display = "none";
    // }
    $("#chat").fadeToggle("slow");
  });
});
