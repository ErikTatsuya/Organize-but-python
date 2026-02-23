let backend;

new QWebChannel(qt.webChannelTransport, function (channel) {
	backend = channel.objects.backend;
});

function chamarPython() {
	backend.somar(5, 7).then(function (resultado) {
		document.getElementById("resultado").innerText =
			"Resultado: " + resultado;
	});
}
