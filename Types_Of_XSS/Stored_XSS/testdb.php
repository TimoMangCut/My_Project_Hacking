<?php
$conn = pg_connect("host=localhost dbname=phuc port=5432 user=postgres password=phuciutram123");
$sql = 'select name from conmeo';
$query = pg_query($conn,$sql);
$result = pg_fetch_assoc($query);
pg_close($conn);
return $result;
