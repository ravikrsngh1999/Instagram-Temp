




var element = document.getElementsByClassName('like-btn')
console.log(element)

for (var i = 0; i < element.length; i++) {
  element[i].addEventListener('click',like)
}

function like(e){
  var s = e.target.src
  if (s.includes('liked.png')) {
    console.log("Dislike Image")
    e.target.src = "img/like.png"
  } else {
    console.log("Like the image")
    e.target.src = "img/liked.png"
  }
}
