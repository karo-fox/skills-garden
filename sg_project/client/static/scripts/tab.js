function tab(listUrl, type, form, formUrl) {
  createList(listUrl, type);
  $(".tab-item").on("click", function(e) {
    $(this).addClass("is-active").siblings().removeClass("is-active");
    if(this.id === "list") {
      createList(listUrl, type);
    } else if(this.id === "create") {
      createForm(form, formUrl);
    } else if(this.id === "journal") {
      $('.main-section').html('<p>Journal</p>');
    } else {
      console.log("none");
    }
  });
}


function createList(url, type) {
  $.getJSON(url, function(data) {
    objects = data.map(function(item) {
      if(type === 'fields' || type === 'topics') {
        return `<div class="block"><a href="${item.url}"><button class=" level button is-black is-fullwidth"><div class="level-left">${item.name}</div><div class="left-right">${item.last_reviewed}</div></button></a></div>`;
      } else if(type === 'sources') {
        return `<div class="block">Source</div>`;
      }
    });
    $('.main-section').html(objects);
  });
};


function createForm(content, url) {
  let form = `<form id="createForm" method="POST">${content}<input type="submit" value="submit" class="button is-black"></form>`;
  $('.main-section').html(form);
  $('#createForm').submit(function(e) {
    e.preventDefault();
    let form = $(this);
    $.ajax({
      url: url,
      method: "POST",
      data: form.serialize(),
    }).done(function() {
      console.log('done');
    });
  });
}