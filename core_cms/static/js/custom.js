

window.onscroll = function() {ProgressScroll()};

function ProgressScroll() {
  let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let scrolled = (winScroll / height) * 100;
  document.getElementById("nav-progress-bar").style.width = scrolled + "%";
}

