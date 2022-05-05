const list = document.querySelectorAll(".bounding_box");
list.forEach(item => item.addEventListener("click", function () {
	list.forEach(item => item.classList.remove("selectedcat"));
	this.classList.add("selectedcat");
}));