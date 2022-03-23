window.onload=function() {
  document.getElementById("a").onchange=function() {
    document.getElementById("b").value=this.options[this.selectedIndex].getAttribute("data-sync");
  }
  document.getElementById("a").onchange(); // trigger when loading
}