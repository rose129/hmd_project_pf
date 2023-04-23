(function() {
  var csrftoken = Cookies.get('csrftoken');
  var likeForm = document.querySelector('.like-form');
  var likeButton = likeForm.querySelector('.like-button');
  var likeCount = likeForm.querySelector('.like-count');

  likeForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          likeButton.classList.toggle('liked', response.liked);
          likeCount.textContent = response.count;
        }
      }
    };
    xhr.open('POST', likeForm.action);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.send();
  });
})();
