$(document).ready(function() {
    $(".text-body-secondary").click(function() {
      let idButton = $(this).attr("id");
      $("#detalles" + idButton).css("display", "flex");
    });


    $(".btn-close").click(function() {
        $(".detalles").css("display", "none");
    });
  });