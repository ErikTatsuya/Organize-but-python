let backend = null;
let dir_path = null;

document.addEventListener("DOMContentLoaded", function () {
	new QWebChannel(qt.webChannelTransport, function (channel) {
		backend = channel.objects.backend;
		console.log("Backend conected.");
	});
});

async function chooseDirPath() {
	if (!backend) return;

	dir_path = await backend.select_dir_path();

	document.getElementById("result").textContent =
		`Pasta selecionada: ${dir_path}`;
}

async function organizeDir() {
	if (!backend) return;

	if (!dir_path) {
		document.getElementById("result").textContent =
			"Por favor, selecione uma pasta primeiro.";
		return;
	}

	await backend.organize_files(dir_path);

	dir_path = null;

	document.getElementById("result").textContent = "Arquivos organizados";
}
