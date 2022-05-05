const list = document.querySelectorAll('.bounding_box');
function activeLink(){
	list.forEach((item) =>
  item.classList.remove('selectedcat'));
  this.classList.add('selectedcat');
}
list.forEach((item) =>
item.addEventListener('click',activeLink)); 