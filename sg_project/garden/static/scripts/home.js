
async function loadData(url) {
  let response = await fetch(url);
  let fields = await response.json();
  return fields;
}

function createObjectsListElem(objectsList) {
  let ul = document.createElement('ul');
  let list = "";
  objectsList.forEach((item, index, array) => {
    list += `<li>${item.name}</li>`;
  });
  ul.innerHTML = list;
  return ul
}

loadData('/garden/1/')
  .then(resolve => {
    let ol = createObjectsListElem(resolve.topics);
    let parent = document.getElementById('objects-list');
    parent.insertAdjacentElement('afterbegin', ol);
  })
  .catch(error => console.log(`ERROR: ${error}`));