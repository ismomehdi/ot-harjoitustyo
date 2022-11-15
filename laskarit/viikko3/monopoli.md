## Monopoli: Sovelluslogiikka

```mermaid
  classDiagram
    Pelaaja "2..8" --> Pelilauta
    Pelaaja --> "2" Noppa
    Pelilauta --> "40" Ruutu
    
    Ruutu --> Aloitusruutu
    Ruutu --> Vankila
    Ruutu --> Sattuma_ja_yhteismaa
    Ruutu --> Asemat_ja_laitokset
    Ruutu --> Normaalit_kadut
    
    Sattuma_ja_yhteismaa --> Kortti
    
    class Pelaaja{
      id
      nappula
      ruutu_id
      rahaa
      heitä_nopat()
      siirrä_nappulaa()
      rakenna_talo()
      rakenna_hotelli()
    }
    
    class Ruutu{
      id
      seuraava_id
      edellinen_id
      tyyppi
    }
    
    class Noppa{
      id
      luku
      heitä_noppaa()
    }
    
    class Pelilauta{ 
      aloitusruutu
      vankila
      etsi_ruutu()
    }
    
    class Normaalit_kadut{
      id
      nimi
      omistaja
      talot : int
      hotelli : bool
    }
    
    class Kortti{
      id
      toiminto
    }
    
    
````
