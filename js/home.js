




var element = document.getElementsByClassName('like-btn')
console.log(element)

for (var i = 0; i < element.length; i++) {
  element[i].addEventListener('click',like)
}

function like(e){
  e.target.src = "img/liked.png"
  console.log(e.target.src)
}
