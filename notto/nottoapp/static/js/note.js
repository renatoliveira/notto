// Underscore.js debounce
function debounce(func, wait, immediate) {
  var timeout;
  return function() {
    var context = this, args = arguments;
    var later = function() {
      timeout = null;
      if (!immediate) func.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
    if (callNow) func.apply(context, args);
  };
};
// Auto update
var debounceStatus = null
function save (status, content) {
  var http = new XMLHttpRequest();
  var url = "{{note_url}}";
  var data = new FormData();
  data.append('content', content);
  data.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

  http.open("POST", url, true);
  http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
      clearTimeout(debounceStatus);
      debounceStatus = setTimeout(function () {
        status.classList.remove('loading')
      }, 300)
    }
  };
  status.innerText = 'Loading...'
  status.classList.add('loading')
  http.send(data);
}
function updatePosition () {
  var toolbar = document.querySelector('.ql-toolbar');
  var editor = document.querySelector('.ql-editor');
  var measures = toolbar.getBoundingClientRect()
  editor.style.padding = measures.height + 'px 0px 0px 0px'
}

// reference: https://codepen.io/quill/pen/kXRjQJ
Quill.prototype.getHtml = function () {
  return this.container.querySelector('.ql-editor').innerHTML;
}
Quill.prototype.setHtml = function (val) {
  return this.container.querySelector('.ql-editor').innerHTML = val;
}
var q = new Quill('#editor', {
  modules: {
    toolbar: {
      container: [
        [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
        ['bold', 'italic', 'underline', 'link'],
        [{ list: 'ordered' }, { list: 'bullet'}],
        ['clean', 'status']
      ],
      handlers: {
        'status': function (){}
      }
    },
  },
  theme: 'snow'
});
var parser = new DOMParser;
var content = window.content
if (content != '') {
  q.setHtml(parser.parseFromString(content, 'text/html').body.textContent);
}
updatePosition()
window.addEventListener('resize', updatePosition)

setTimeout(function () {
  q.on('text-change', debounce(function() {
    save(document.querySelector('.ql-status'), q.getHtml());
  }, 250));
})
