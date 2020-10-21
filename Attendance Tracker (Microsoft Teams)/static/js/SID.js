$(function () {
    $("#btnSubmit").click(function () {
      var SecretID1 ={{ SecretID }};
      var sid = $("#SecretID").val();
      if (sid != SecretID1) {
                  alert("secret ID do not match.");
                  return false;
              }
              return true;
    });
});
  