$(document).ready(function () {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
    let films = data.results;
    for (let film of films) {
      $("ul#list_movies").append(`<li>${film.title}</li>`);
    }
  });
});
