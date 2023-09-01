<!DOCTYPE html>
<html>
<head>
    <title>LTI.UY_demo-1.0.0-pre-alpha</title>
</head>
<body>
    <form method="post" action="index.php">
        <label for="usuario">Usuario:</label>
        <input type="text" name="usuario" id="usuario">
        <br><br>
        <label for="passwd">Contraseña:</label>
        <input type="password" name="passwd" id="passwd">
        <br><br>
        <input type="submit" value="Iniciar sesión" name="login">
    </form>
<?php
if (isset($_POST['login'])) {
    echo "<br><br>";

    $usuario = $_POST['usuario'];
    $passwd = $_POST['passwd'];

    function modules($module,$user,$pswrd) {
        if ($module !== "") {
            $mod = $module . ' ' . $user . ' ' . $pswrd;
            $output = [];
            $exit_code = 0;
            exec($mod, $output, $exit_code);
            if ($exit_code != 0) {
                http_response_code(404);
                $output[0] = "Error en el script de Portal Académico.<br>";
            } 
        } else {
            http_response_code(404);
            $output[0] = "Error en el script de Portal Académico.<br>";
        }
        return $output;
    }

    $portal = modules('python C:\xampp\htdocs\demo-1.0.0-pre-alpha\1-PortalAcademico-v1.1_pp.py',$usuario,$passwd);
    foreach ($portal as $message) {
        print($message . "<br>");
    }

    $moodle = modules('python C:\xampp\htdocs\demo-1.0.0-pre-alpha\2-Moodle-EVA-v1.0_pp.py',$usuario,$passwd);
    foreach ($moodle as $message) {
        print($message . "<br>");
    }


    # convertir los dos script a funciones
    # convertir los scripts a funciones y llamarlas desde este mismo script con include_once, pasarles las credenciales como argumentos

    # The user has already reached the maximum allowed number of sessions. 
    # Please close one of the existing sessions before trying to login again.
}
?>
</body>
</html>

