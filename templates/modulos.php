<!DOCTYPE html>
<html>
    <head>
        <title>TriTechDataLab</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
    </head>
    <header>
        <h1>Módulos</h1>
        <nav>
            <ul>
                <li><a href="index.php">Início</a></li>
                <li><a href="modulos.php">Módulos</a></li>
                <li><a href="bibliotecas.php">Bibliotecas</a></li>
                <li><a href="about.php">About Us</a></li>
            </ul>
        </nav>
    </header>
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
    <footer>
        <p>&copy; 2023 TTDL </p>
    </footer>
</html>