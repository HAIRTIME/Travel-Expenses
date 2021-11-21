<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title>User: {{user}}</title>
</head>
<body>
    <table cellspacing="12">
        <tr>
            <th>Trip ID</th><th>Name</th><th>Date</th><th>Destination</th><th>Miles</th><th>Gallons</th>
        </tr>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
        </tr>
        %end
    </table>

</body>
</html>