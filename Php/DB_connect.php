<?php

try
{
	$db=new PDO("mysql:host=localhost;dbname=veritabanı;charset=utf8",'kullanıcı','sifre');
//	echo "baglanti basarili";
}
catch(PDOException $e)
{
	echo $e->getMessage();
}


?>
