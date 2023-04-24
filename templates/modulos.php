<!DOCTYPE html>
<html>
<head>
	<title>TriTechDataLab</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="style.css">
</head>

<?php
	include_once('header_footer/header.php')
?>

<body>
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
</body>

</html>


<?php
	include_once('header_footer/footer.php')
?>