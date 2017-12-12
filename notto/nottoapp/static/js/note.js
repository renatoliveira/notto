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
  var url = window.notto.note.url;
  var data = new FormData();
  data.append('content', content);
  data.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

  http.open("POST", window.location.origin + '/' + url, true);
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
function setupChildren () {
  var children = window.notto.note.children
  var childrenNav = document.querySelector('.note-children')
  if (!children.length) return childrenNav.classList.add('--hidden')
  var icons = {
    'folder': '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M9.984 3.984l2.016 2.016h8.016c1.078 0 1.969 0.938 1.969 2.016v9.984c0 1.078-0.891 2.016-1.969 2.016h-16.031c-1.078 0-1.969-0.938-1.969-2.016v-12c0-1.078 0.891-2.016 1.969-2.016h6z"></path></svg>',
    'file': '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20.016 18v-9.984h-16.031v9.984h16.031zM20.016 6c1.078 0 1.969 0.938 1.969 2.016v9.984c0 1.078-0.891 2.016-1.969 2.016h-16.031c-1.078 0-1.969-0.938-1.969-2.016v-12c0-1.078 0.891-2.016 1.969-2.016h6l2.016 2.016h8.016z"></path></svg>',
    'link': '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="640" height="640" viewBox="0 0 640 640"><path fill="#000" d="M251.488 470.112l-25.92 25.76c-22.432 22.24-58.976 22.24-81.44 0-10.752-10.688-16.672-24.928-16.672-40.064s5.952-29.312 16.672-40.064l95.36-94.56c19.744-19.616 56.928-48.48 84.032-21.6 12.448 12.352 32.512 12.288 44.896-0.16 12.32-12.448 12.256-32.544-0.192-44.864-46.016-45.696-114.112-37.248-173.408 21.6l-95.36 94.592c-22.88 22.688-35.456 52.928-35.456 85.056 0 32.192 12.608 62.368 35.456 85.056 23.552 23.36 54.464 35.072 85.408 35.072s61.888-11.68 85.408-35.072l25.952-25.76c12.448-12.32 12.512-32.384 0.16-44.8-12.384-12.416-32.448-12.48-44.896-0.192zM540.512 102.624c-49.504-49.088-118.688-51.744-164.448-6.304l-32.288 32.064c-12.448 12.352-12.544 32.416-0.192 44.832 12.352 12.448 32.416 12.512 44.864 0.16l32.32-32.032c23.68-23.552 54.752-13.792 75.072 6.304 10.752 10.72 16.704 24.928 16.704 40.064s-5.952 29.344-16.704 40.032l-101.76 100.928c-46.528 46.112-68.352 24.512-77.664 15.264-12.448-12.352-32.512-12.256-44.832 0.16-12.352 12.448-12.288 32.544 0.16 44.832 21.376 21.184 45.76 31.68 71.296 31.68 31.264 0 64.32-15.744 95.776-46.944l101.76-100.896c22.784-22.72 35.424-52.928 35.424-85.056 0-32.16-12.64-62.368-35.488-85.088z"></path></svg>'
  }
  var createLists = function (children) {
    var list = document.createElement('ul')
    children.forEach(function (child) {
      var iconType = child.children.length ? 'folder' : 'file'
      var item = document.createElement('li')
      item.classList.add(iconType)
      var itemHTML = '<i class="icon ' + iconType + '">' + icons[iconType] + '</i>'
      if (child.children.length) {
        itemHTML += '<span class="path">' + child.name + '</span>'
        itemHTML += '<a class="icon link" href="' + child.path + '">' + icons.link + '</a>'
      } else {
        itemHTML += '<a class="path" href="' + child.path + '">' + child.name + '</a>'
      }

      item.innerHTML = itemHTML
      if (child.children.length) {
        item.appendChild(createLists(child.children))
      }
      item.addEventListener('click', function (e) {
        e.stopPropagation()
        var childList = item.querySelector(':scope ul')
        if (childList) {
          if (childList.classList.contains('visible')) {
            childList.classList.remove('visible')
          } else {
            childList.classList.add('visible')
          }
        }
      })
      list.appendChild(item)
    })
    return list
  }
  var getPathLevel = function (str) {
    return str.split('/').length - 1
  }
  var mappedChildren = {}
  var comparePaths = function (pathA, pathB) {
    pathA = pathA.split('/')
    pathB = pathB.split('/')
    return pathA.filter(function (pathASlice, index) {
      return pathB[index] === pathASlice
    }).length === pathA.length
  }
  var mapChildren = function (children, parent) {
    return children.map(function (child) {
      if (mappedChildren[child.url_title]) return null
      child = {
        path: child.url_title,
        name: parent ? child.url_title.replace(parent.path, '') : child.url_title.replace(window.location.pathname.substr(1), ''),
        level: getPathLevel(child.url_title)
      }
      child.children = children.filter(function (_child) {
        return comparePaths(child.path, _child.url_title) && getPathLevel(_child.url_title) > child.level
      })
      if (child.children.length) {
        child.children = mapChildren(child.children, child)
        return child
      }
      return child
    }).filter(function (child) {
      if (child) mappedChildren[child.path] = true
      return child !== null
    })
  }
  var navigation = document.createElement('nav')
  children = children.map(function (child) {
    child.url_title = child.url_title.substr(0)
    return child
  })
  childrenNav.appendChild(createLists(mapChildren(children)))
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
var content = window.notto.note.content
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

setupChildren()
