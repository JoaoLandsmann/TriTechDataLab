<!DOCTYPE html>
<html>
<head>
	<title>TriTechDataLab</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<header>
		<h1>Biblioteca</h1>
		<nav>
			<ul>
				<li><a href="#">Início</a></li>
				<li><a href="#">Catálogo</a></li>
				<li><a href="#">Minha Conta</a></li>
				<li><a href="#">Sobre Nós</a></li>
			</ul>
		</nav>
	</header>

	<main>
		<table>
			<tr>
				<th>Id</th>
				<th>Nome</th>
				<th>Descrição</th>
			</tr>
			{% for row in data %}
			<tr>
				<td>{{ row[0] }}</td>
				<td>{{ row[1] }}</td>
				<td>{{ row[2] }}</td>
			</tr>
			{% endfor %}
		</table>
	</main>

	<footer>
		<p>&copy; 2023 TTDL </p>
	</footer>
</body>
</html>