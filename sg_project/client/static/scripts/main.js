const csrftoken = getCookie('csrftoken');
const host = 'http://127.0.0.1:8000'

function tab(listUrl, type, form) {
  if(type === "fields" || type === "topics") {
    createList(listUrl);
  } else if(type === "sources") {
    createSourceList(listUrl);
  }
  $(".tab-item").on("click", function(e) {
    $(this).addClass("is-active").siblings().removeClass("is-active");
    if(this.id === "list") {
      if(type === "fields" || type === "topics") {
        createList(listUrl);
      } else if(type === "sources") {
        createSourceList(listUrl);
      }
    } else if(this.id === "create") {
      if(type === "fields" || type === "topics") {
        createForm(form, listUrl, '.main-section');
      } else if(type === "sources") {
        createSourceForm(form, listUrl);
      }
    }
  });
}

function actionButtons(url, backUrl, editForm) {
  $('#delete').click(function() {
    $.ajax({
      url: `${host}/${url}/action/`,
      headers: {'X-CSRFToken': csrftoken},
      method: "DELETE"
    }).done(function() {
      window.location.href = `${host}/${backUrl}`;
    });
  });
  
  $('#edit').click(function() {
    $('.modal').addClass("is-active");
    $('#editFormBlock').html(editForm);
    $('#editForm').submit(function(e) {
      e.preventDefault();
      let form = $(this);
      $.ajax({
        url: `${host}/${url}/action/`,
        method: "PUT",
        headers: {'X-CSRFToken': csrftoken},
        data: form.serialize(),
      }).done(function() {
        window.location.href = `${host}/${backUrl}`;
      });
    });
    $('.modal-background').on('click', function() {
      $('.modal').removeClass("is-active");
    })
  });
}


function createList(url) {
  $.getJSON(`${host}/${url}/`, function(data) {
    objects = data.map(function(item) {
      return `<div class="block"><a href="${item.url}"><div class="level box"><div class="level-left">${item.name}</div><div class="left-right">${item.last_reviewed}</div></div></a></div>`;
    });
    $('.main-section').html(objects);
  });
}


function createSourceList(url) {
  $('.main-section').html(`
  <div class="buttons">
    <button id="text" class="button is-black">Notes</button>
    <button id="urls" class="button is-black">Links</button>
  </div>
  <div id="text-sources"></div>
  <div id="url-sources"></div>
  `);
  getTextSources(url);
  $('#text').click(function() {
    $('#url-sources').html('');
    getTextSources(url);
  });
  $('#urls').click(function() {
    $('#text-sources').html('');
    getURLSources(url);
  });
}


function getTextSources(url) {
  $.getJSON(`${host}/${url}/text/`, function(data) {
    sources = data.map(function(item) {
      return `
      <div class="block box">
        <div class="level">
          <div class="title is-4 level-left">${item.name}</div>
          <div class="buttons level-right">
            <button id="edit-text-source-${item.id}" class="button is-link textEdit">Edit</button>
            <button id="delete-text-source-${item.id}" class="button is-danger textDelete">Delete</button>
          </div>
        </div>
        <p>${item.content}</p>
      </div>`;
    });
    $('#text-sources').html(sources);
    $('.textEdit').click(function() {
      let id_attr = $(this).attr("id");
      let id = id_attr.match(/\d+/);
      console.log(`text edit was clicked with id: ${id}`);
    });
    $('.textDelete').click(function() {
      let id = $(this).attr("id");
      console.log('text delete was clicked');
    });
  });
}

function getURLSources(url) {
  console.log(`url in getURLSources: ${url}`);
  $.getJSON(`${host}/${url}/url/`, function(data) {
    sources = data.map(function(item) {
      return `
      <div class="block box">
        <div class="level">
          <div class="title is-4 level-left">${item.name}</div>
          <div class="buttons level-right">
            <button id="edit-url-source-${item.id}" class="button is-link urlEdit">Edit</button>
            <button id="delete-url-source-${item.id}" class="button is-danger urlDelete">Delete</button>
          </div>
        </div>
        <a href="${item.content}" target="_blank" rel="noopener noreferrer">${item.content}</a>
      </div>`;
    });
    $('#url-sources').html(sources);
    $('.urlEdit').click(function() {
      let id = $(this).attr("id");
      console.log('url edit was clicked');
    });
    $('.urlDelete').click(function() {
      let id = $(this).attr("id");
      console.log('url delete was clicked');
    });
  });
}


function createForm(content, url, where) {
  let form = `<form id="createForm" method="POST">${content}<input type="submit" value="submit" class="button is-black"></form>`;
  $(where).html(form);
  $('#createForm').submit(function(e) {
    e.preventDefault();
    let form = $(this);
    $.ajax({
      url: `${host}/${url}/`,
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


function createSourceForm(content, url) {
  $('.main-section').html(`
  <div class="buttons">
    <button id="create-text" class="button is-black">New note</button>
    <button id="create-urls" class="button is-black">New link</button>
  </div>
  <div id="text-form"></div>
  <div id="url-form"></div>
  `);
  createForm(content[0], `${url}/text`, '#text-form');
  $('#create-text').click(function() {
    $('#url-form').html('');
    createForm(content[0], `${url}/text`, '#text-form');
  });
  $('#create-urls').click(function() {
    $('#text-form').html('');
    createForm(content[1], `${url}/url`, '#url-form');
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
