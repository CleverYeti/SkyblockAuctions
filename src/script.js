
// search settings
let cat_filter = "allcat";
let search_filter = "";
let sort = "lowest";
let rarity_filter = "any";
let bin_filter = "any";

// input elements
const search_element = document.getElementById("searchinput");
const sort_element = document.getElementById("sort");
const rarity_element = document.getElementById("rarityfilter");
const bin_element = document.getElementById("binfilter");

// function that reloads the auctions
function reload_auctions() {
	search_filter = search_element.value;
	sort = sort_element.value;
	rarity_filter = rarity_element.value;
	bin_filter = bin_element.value;
	
	console.log(cat_filter);
	console.log(search_filter);
	console.log(sort);
	console.log(rarity_filter);
	console.log(bin_filter);
	
	console.log("reload called");
}

// clickable category buttons
const list = document.querySelectorAll(".bounding_box");
list.forEach(item => item.addEventListener("click", function () {
	list.forEach(item => item.classList.remove("selectedcat"));
	this.classList.add("selectedcat");
	cat_filter = String(this.id);
	reload_auctions();
}));

