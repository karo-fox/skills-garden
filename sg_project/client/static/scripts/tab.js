function tab(listUrl, type, form, formUrl, id, token) {
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
  const csrftoken = getCookie('csrftoken');
  $('#delete').click(function(e) {
    $.ajax({
      url: `../garden/${id}/delete/`,
      headers: {'X-CSRFToken': csrftoken},
      method: "DELETE"
    }).done(function() {
      console.log('field was destroyed');
      window.location.href = '/';
    });
  });
  
  $('#edit').click(function(e) {
    console.log('edit was clicked');
  });
}


function createList(url, type) {
  $.getJSON(url, function(data) {
    objects = data.map(function(item) {
      if(type === 'fields' || type === 'topics') {
        return `<div class="block"><a href="${item.url}"><div class="level box"><div class="level-left">${item.name}</div><div class="left-right">${item.last_reviewed}</div></div></a></div>`;
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
      $('.main-section').prepend('<div id="FormSubmitted" class="notification"><button id="deleteButton" class="delete"></button>Form was submitted</div>');
      $('#deleteButton').on("click", function(e) {
        $('#FormSubmitted').remove();
      });
    });
  });
  
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
