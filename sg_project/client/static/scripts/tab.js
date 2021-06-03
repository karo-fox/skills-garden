$(document).ready(function() {
  createList('/garden/fields/');
  $(".tab-item").on("click", function(e) {
    $(this).addClass("is-active").siblings().removeClass("is-active");
    if(this.id === "list") {
      createList('/garden/fields/');
    } else if(this.id === "create") {
      $('.main-section').html('<p>Create Form</p>');
    } else if(this.id === "journal") {
      $('.main-section').html('<p>Journal</p>');
    } else {
      console.log("none");
    }
  });
});

function createList(url) {
  let objects = []
  $.getJSON(url, function(data) {
    objects = data.map(function(item) {
      return `<div class="block"><a href="${item.url}"><button class=" level button is-black is-fullwidth"><div class="level-left">${item.name}</div><div class="left-right">${item.last_reviewed}</div></button></a></div>`
    });
    $('.main-section').html(objects);
  });
};