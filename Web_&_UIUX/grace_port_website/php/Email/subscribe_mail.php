<?php
if($_POST["client_subscrible_mail"]){
    $client_mail = $_POST["client_subscrible_mail"];
    $to = "your@gmail.com";
    //fsgpmp@caritassws.org.hk
    $subject = "New Subscrible ";

    $message = "
    <html>
    <head>
    <title>CinLinG Check Email la !!</title>
    </head>
    <body>
    <p>New email: ".$client_mail."</p>
    </body>
    </html>
    ";

    $headers = "From: ".$client_mail."\r\n";
    $headers .= "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

    if (mail($to, $subject, $message, $headers)){
        ?>
        <script language="javascript" type="text/javascript">
         // redirect to contact_us
        alert('Success! Thank you');
        history.back();
        </script>
        <?php
    } else{
        //mail failed for some reason
        ?>
        <script language="javascript" type="text/javascript">
            alert('Message failed. Try again or other way');
            history.back();
            </script>
        <?php
    }
}else{
    ?>
    <script language="javascript" type="text/javascript">
    //redirect to contact_us
    alert('Please input Email');
    history.back();;
    </script>
    <?php
}


?>