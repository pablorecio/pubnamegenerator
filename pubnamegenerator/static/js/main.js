var getPubName = function() {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/api/pub');
	xhr.onreadystatechange = function () {
		if (xhr.readyState !== 4 || xhr.status !== 200)
			return;

		var pub = JSON.parse(xhr.responseText);
		document.getElementById('pub-name').innerHTML = pub.name;
	};
	xhr.send(null);
};

window.onload = function() {
	var button = document.getElementById('another-pub');
	button.addEventListener('click', function() {
		getPubName();
	});

	getPubName();
};