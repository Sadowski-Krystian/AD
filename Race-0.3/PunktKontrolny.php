<?php
class PunktKontrolny{
	
	private $id;
	private $zespol;
	private $punktyDostepne = 100;	// pkt
	private $punktyZdobyte = 0;
	private $czasDostepny = 10*60;	// min/sek = (10*60)
	private $czasRealizacji = 0;	// min/sek
	private $nazwa;
	private $opis;
	
	public function __construct( int $id, string $nazwa ){
		$this->id = $id;
		$this->nazwa = $nazwa;
	}
	public function ustalPunkty( int $wartosc ){
		$this->punktyDostepne = $wartosc;
	}
	public function zamelduj( int $idZesp ){
		$ts = date("Y-m-d H:i:s");	// 2022-05-31 08:28:08
		$this->zespol = array('id'=>$idZesp,'czasWe'=>$ts );
	}
	public function odmelduj( int $idZesp ){
		$ts = date("Y-m-d H:i:s");	// 2022-05-31 08:28:08
		$this->zespol['czasWy'] = $ts+515;
	}
	public function zalicz(){
		$this->odmelduj($this->zespol['id']);
		$this->obliczPunkty();
	}
	private function obliczPunkty(){
		# $czasDostepny = 3*60; // min
		# $punktyDostepne = 360; //pkt
		# $czasRealizacji = 90; // sek -> 180 pkt
		#echo strtotime($this->zespol['czasWe']);		echo '<br/>';
		#echo strtotime($this->zespol['czasWy']);		echo '<hr/>';
		$this->czasRealizacji = (int)$this->zespol['czasWy']-(int)$this->zespol['czasWe'];
		$pkt = $this->czasDostepny-$this->czasRealizacji;
		$pkt = $pkt/10;
		#var_dump($this->czasDostepny);		var_dump($this->czasRealizacji);		var_dump($pkt);
		$this->punktyZdobyte = $pkt;
	}
	public function wyswietlOpis(){
		$rn = "<br/>\r\n";
		$out = 'Punkt kontrolny #'.$this->id.$rn;
		$out.= 'Nazwa: '.$this->nazwa.$rn;
		$out.= 'Punkty: '.$this->punktyDostepne.$rn;
		$out.= 'PunktyZdobyte: '.$this->punktyZdobyte.$rn;
		return $out;
	}
}
?>






