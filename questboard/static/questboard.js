$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal .modal-content").html("");
        $("#modal").modal("show");
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#table tbody").html(data.html_list);
          $("#modal").modal("hide");
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  // Create questboard
  $(".js-create-questboard").click(loadForm);
  $("#modal").on("submit", ".js-questboard-create-form", saveForm);

  // Edit questboard
  $("#table").on("click", ".js-edit-questboard", loadForm);
  $("#modal").on("submit", ".js-questboard-edit-form", saveForm);

  // Delete questboard
  $("#table").on("click", ".js-delete-questboard", loadForm);
  $("#modal").on("submit", ".js-questboard-delete-form", saveForm);

});