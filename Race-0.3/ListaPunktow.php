<?php
class ListaPunktow {
	
	private $lista = array();
	
	public function __construct(){
		print("Treśćxx<br/>");
	}
	
	public function dodaj( $pk )
	{	// dodaj do listy[] punkt kontrolny
		$this->lista[] = $pk;
	}
	public function wyswietl()
	{	// wygeneruj kod HTML z listą PK
		$out = '';		#var_dump($this->lista);
		foreach( $this->lista as $key => $obj){		#for( $i=0; $i<count($this->lista); $i++){	#	$out.= $this->lista[$i].'<br/>';	#	$out.= "Klucz: {$key}";
			$out.= $obj->wyswietlOpis();
		}
		return $out;
	}
	
}
?>
