let backend = null;
let dir_path = null;
let input = document.getElementById("dirPathInput");
let result = document.getElementById("result");

document.addEventListener("DOMContentLoaded", function () {
	new QWebChannel(qt.webChannelTransport, function (channel) {
		backend = channel.objects.backend;
		console.log("Backend conected.");
	});
});

async function chooseDirPath() {
	if (!backend) return;

	dir_path = await backend.select_dir_path();

	result.textContent = `Pasta selecionada: ${dir_path}`;
	input.value = dir_path;
}

async function organizeDir() {
	if (!backend) return;

	if (!dir_path) {
		result.textContent = "Por favor, selecione uma pasta primeiro.";
		input.value = "";
		return;
	}

	await backend.organize_files(dir_path);

	dir_path = null;

	result.textContent = "Arquivos organizados";
	input.value = "";
}
