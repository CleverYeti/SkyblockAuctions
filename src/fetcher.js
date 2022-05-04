/*
"use strict";
fetch("https://api.hypixel.net/skyblock/auctions").then(response => response.json()).then((json) => {
	let auctions = json["auctions"];
	console.log(json["totalPages"]);
	// TODO: something useful with auctions
	const tiers = new Map();
	for (const auction of auctions) {

	}
	console.log(auctions[69]["tier"]);
}).catch(err => console.log(err));

*/