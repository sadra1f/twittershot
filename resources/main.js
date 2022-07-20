function getTimeAsString() {
  let date = new Date();
  let hours = date.getHours().toString();
  if (hours.length < 2) hours = "0" + hours;
  let minutes = date.getMinutes().toString();
  if (minutes.length < 2) minutes = "0" + minutes;
  let seconds = date.getSeconds().toString();
  if (seconds.length < 2) seconds = "0" + seconds;
  return hours + ":" + minutes + ":" + seconds;
}

window.addEventListener("pywebviewready", function () {
  let urlElement = document.getElementById("url");
  let submitElement = document.getElementById("submit");
  let logElement = document.getElementById("log");

  let log = function (content) {
    logElement.innerHTML += "[" + getTimeAsString() + "] " + content + "\n";
  };

  submitElement.addEventListener("click", function () {
    let url = urlElement.value;
    urlElement.value = "";

    if (url && url != "") {
      log("Rendering " + url);
      pywebview.api.render(url);
    }
  });

  log("App started.");
});
