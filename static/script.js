function rangeSlide(value) {
  document.getElementById('rangeValue').innerHTML = value;
}

document.addEventListener("DOMContentLoaded", function() {
  var form = document.getElementById("mainform");
  var input = document.getElementById("slider");
  var modal = document.getElementById("myModal");
  var span = document.getElementsByClassName("close")[0];

  form.addEventListener('submit', function(e) {
    input.value = "your_var";
    form.submit();
    modal.style.display = "flex";
  });

  span.onclick = function() {
    modal.style.display = "none";
    window.location.href = '/modal';
  };

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
      window.location.href = '/modal';
    }
  };
});