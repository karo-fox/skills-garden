function tab(url, type) {
  createList(url, type);
  $(".tab-item").on("click", function(e) {
    $(this).addClass("is-active").siblings().removeClass("is-active");
    if(this.id === "list") {
      createList(url, type);
    } else if(this.id === "create") {
      $('.main-section').html('<p>Create Form</p>');
    } else if(this.id === "journal") {
      $('.main-section').html('<p>Journal</p>');
    } else {
      console.log("none");
    }
  });
}

function createList(url, type) {
  console.log(type);
  $.getJSON(url, function(data) {
    objects = data.map(function(item) {
      if(type === 'fields' || type === 'topics') {
        return `<div class="block"><a href="${item.url}"><button class=" level button is-black is-fullwidth"><div class="level-left">${item.name}</div><div class="left-right">${item.last_reviewed}</div></button></a></div>`
      } else if(type === 'sources') {
        return `<div class="block">Source</div>`;
      }
    });
    $('.main-section').html(objects);
  });
};