<?php
class PunktKontrolny{
	/** @var int $id przechowuje id */
	private $id;
	/** @var array $zespol przechowuje zespół */
	private $zespol;
	/** @var int $punktyDostepne przechowuje dostępne kunkty */
	private $punktyDostepne = 100;	// pkt
	/** @var int $punktyZdobyte przechowuje zdobyte kunkty */
	private $punktyZdobyte = 0;
	/** @var int $czasDostepny przechowuje dostępny czas */
	private $czasDostepny = 10*60;	// min/sek = (10*60)
	/** @var int $czasRealizacji przechowuje czas realizacji */
	private $czasRealizacji = 0;	// min/sek
	/** @var String $nazwa przechowuje nazwe */
	private $nazwa;
	/** @var String $opis przechowuje opis */
	private $opis;
	
	public function __construct( int $id, string $nazwa ){
		$this->id = $id;
		$this->nazwa = $nazwa;
	}
	/**
	  * ustala dostępne kunkty
     * @param Int $wartosc ilośc dostępnych punktów
     */
	public function ustalPunkty( int $wartosc ){
		$this->punktyDostepne = $wartosc;
	}
	/**
	  * ustawia dany zespół w gotowości
     * @param Int $idZesp id zespołu do zameldowania
     */
	public function zamelduj( int $idZesp ){
		$ts = date("Y-m-d H:i:s");	// 2022-05-31 08:28:08
		$this->zespol = array('id'=>$idZesp,'czasWe'=>$ts );
	}
	/**
	  * usuwa zespól z gry
     * @param Int $idZesp id zespołu do odmeldowania
     */
	public function odmelduj( int $idZesp ){
		$ts = date("Y-m-d H:i:s");	// 2022-05-31 08:28:08
		$this->zespol['czasWy'] = $ts+515;
	}
	/**
	  * zlicza pinkty
     * 
     */
	public function zalicz(){
		$this->odmelduj($this->zespol['id']);
		$this->obliczPunkty();
	}
	/**
	  * oblicza punkty na podstawie pozostałego czasu
     */
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
	/**
	  * wyświetla html z opisem
	  * @return String Html z opisem
     */
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






