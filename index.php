<!DOCTYPE html>
<html>
<head>
    <title>Meu site</title>
</head>
<body>
    <h1>Conteúdo da tabela modulos:</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Descrição</th>
            </tr>
        </thead>
        <tbody>
            {% for row in rows %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>