const content = document.querySelector(".md-content__inner");
const virtualList = document.querySelector(".md-content__inner p");
const getNodeHeight = (node) => {
	var height, clone = node.cloneNode(true)
	// hide the meassured (cloned) element
	clone.style.cssText = "position:fixed; top:-9999px; opacity:0;"
	// add the clone to the DOM 
	content.appendChild(clone)
	// meassure it
	height = clone.getBoundingClientRect().height
	// cleaup 
	clone.parentNode.removeChild(clone)
	return height
}
document$.subscribe(async () => {
	virtualList.outerHTML = "<vaadin-virtual-list></vaadin-virtual-list>";
	await import("https://esm.sh/@vaadin/virtual-list/theme/material/vaadin-virtual-list.js");
	const { rows } = await import("/assets/cvars.js");
	virtualList.items = rows;
	virtualList.renderer = (root, list, { item, index }) => {
		const [name, description] = item;
		root.innerHTML =
			`<h3 id="${name}"><strong>${name}</strong><a class="headerlink" href="https://docs.nixware.cc/cvars/#${name}" title="Permanent link">¶</a></h3>
			<p>
				<font size="5">
					<code class="language-typescript highlight"><span class="nx">cvars</span><span class="p">.</span><span class="nx">${name}</span><span class="o">:</span></code>
					<code>convar_t</code>
				</font>
			</p>
			${description ? `<p>${description}</p>` : ""}`;
	}


	// const list = new HyperList(container, {
	// 	itemHeight: 150,
	// 	total: rows.length,
	// 	generate(index) {


	// 		//saving height
	// 		if(!rows[index][2]){
	// 			console.log(name, rows[index][2] = getNodeHeight(element))
	// 		}
	// 		return { element, height: rows[index][2] };
	// 	},
	// 	height: "80vh",
	// 	width: "none"
	// });
})