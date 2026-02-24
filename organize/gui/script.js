let backend;

new QWebChannel(qt.webChannelTransport, function (channel) {
	backend = channel.objects.backend;
});

async function chamarPython() {
	let dir_path = await backend.select_dir_path();

	document.getElementById("resultado").textContent =
		`Pasta selecionada: ${dir_path}`;
}
