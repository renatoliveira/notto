var folders = ['my', 'what', 'some', 'secret', 'safe', 'chuck', 'norris', 'blank']
var wordList = ["done","themselves","settle","wet","military","actual","frame","paid","came","moon","count","finest","bigger","rubbed","nearby","plain","disease","burn","market","they","nor","mouse","rays","choose","line","film","lonely","neighborhood","slave","hunt","quite","bent","construction","copy","thou","cat","characteristic","you","history","negative","which","continent","flew","fair","sport","balloon","give","forty","passage","fix"];
var getAWord = function () {
  return wordList[Math.floor(Math.random() * wordList.length)]
}
var input = document.querySelector('.form-control')
var button = document.querySelector('.button')

input.placeholder = getAWord() + '/' + getAWord()
input.addEventListener('keyup', function (event) {
  var key = event.which || event.keyCode
  var ENTER = 13
  button.href = input.value
  if (key == ENTER) {
    window.location = window.location.origin + '/' + input.value
  }
})
