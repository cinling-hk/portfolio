
<?php
    if($_POST["client_email"]){
        $cname = $_POST["client_name"];
        $cmail = $_POST["client_email"];
        $ctel = $_POST["client_tel"];
        $cq = $_POST["client_question"];

        $to = "fsgpmp@caritassws.org.hk";
        $subject = "New Form Contact From ".$cname;
        $headers = "From: ".$cmail."\r\n";
        $headers .= "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        $message = "
        <html>
        <head>
        <title>CinLinG Check Email la !!</title>
        </head>
        <body>
        <h1>Hi CinLinG</h1>
        <p>".$cname."</p>
        <p>".$cmail."</p>
        <p>".$ctel."</p>
        <p>".$cq."</p>
        </body>
        </html>
        ";

        // ini_set("SMTP","ssl://smtp.gmail.com");
        // ini_set("smtp_port","25");
        
        //SUCCESS OR FAIL FOR CORRECT TEXT
        if (mail($to, $subject, $message, $headers)){
                ?>
            <script language="javascript" type="text/javascript">
            // redirect to contact_us
            alert('Success! Thank you');
            history.back();;
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
