$(document).ready(function() {
    $(".text-body-secondary").click(function() {
      let idButton = $(this).attr("id");
      $("#detalles" + idButton).toggle();
    });


    $(".btn-close").click(function() {
        $(".detalles").hide();
    });
  });