const $ = window.$;
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      const titles = data.results;
      for (const i in titles) {
        $('#list_movies').append(`<li> ${titles[i].title} </li>`);
      }
    }
  });
});
