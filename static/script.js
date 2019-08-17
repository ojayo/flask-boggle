$(function() {

  let score = 0;

  $("#score").append(score)

  $("form").on("submit", async function(evt) {
    evt.preventDefault();

    let guessedWord = $("#guess").val();

    let response = await axios.post("/", {guess: guessedWord} );
    if (response.data.response === "ok") {
      score++;
    }

    $("#message").empty().append(response.data.response);
    $("#score").empty().append(score);
  })

})