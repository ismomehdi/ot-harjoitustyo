## Monopoli: Sovelluslogiikka

```mermaid
  classDiagram
    Pelaaja "2..8" ..> Pelilauta
    Pelilauta ..> "2" Noppa
    Pelilauta --> "40" Ruutu
    
    class Pelaaja{
      id
      nappula
      ruutu_id
    }
    
    class Ruutu{
      id
      seuraava_id
      edellinen_id
    }
    
    class Noppa{
      id
      luku
    }
    
````
