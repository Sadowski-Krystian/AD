<?php
include('ListaPunktow.php');
include('PunktKontrolny.php');
$lp = new ListaPunktow();
$pk1 = new PunktKontrolny(1, 'Dąbrowskiego (ZSE)');
$pk1->ustalPunkty(0);
$pk2 = new PunktKontrolny(2, 'Hawelańska (Luna)');
$pk2->ustalPunkty(50);
$pk2->zamelduj(13);
$pk2->odmelduj(13);
$pk2->zalicz();
//$pk3 = new PunktKontrolny(3, 'Stary most');
$pk4 = new PunktKontrolny(4,'NovaPark');
$pk4->ustalPunkty(150);
$pk4->zamelduj(13);
$pk4->odmelduj(13);
$pk5 = new PunktKontrolny(5,'Grobla 68a');
$pk5->ustalPunkty(250);
$lp->dodaj( $pk1 );
$lp->dodaj( $pk2 );
$lp->dodaj( new PunktKontrolny(3, 'Stary most') );
$lp->dodaj( $pk4 );
$lp->dodaj( $pk5 );
echo $lp->wyswietl();
?>
















