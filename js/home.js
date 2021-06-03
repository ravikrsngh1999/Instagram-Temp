



/* element is having he array of all element of that class */
var element = document.getElementsByClassName('like-btn')
console.log(element)


/* We are adding click event to all the elements */
/* element[i] is an element object */
for (var i = 0; i < element.length; i++) {
  element[i].addEventListener('click',like)
}

/* e contains all the info about the event */
/* e.target is the element object which was clicked */
function like(e){
  var s = e.target.src
  console.log(s)
  if (s.includes('liked.png')) {
    console.log("Dislike Image")
    e.target.src = "img/like.png"
  } else {
    console.log("Like the image")
    e.target.src = "img/liked.png"
  }
}





document.getElementById('profile-btn').addEventListener('click',showmenu)

function showmenu(){
  var s = document.getElementById('menu-box').style.display
  if (s.includes("block")) {
    document.getElementById('menu-box').style.display = "none"
  } else {
    document.getElementById('menu-box').style.display = "block"
  }


}
