# Racism Game

Este projeto implementa uma experiência interativa em que o jogador explora cenas do Google Street View e um mapa temático para descobrir símbolos de combate ao racismo em pontos estratégicos da cidade de São Paulo.

## Funcionalidades

- **Cenas Street View**
  - Cada cena mostra um ponto fixo do Street View.
  - A tela é coberta por um véu em escala de cinza, deixando a cena sem cores. Cobertura pensada para não violar termos de uso das imagens Street View.
  - O jogador deve clicar no local certo para revelar o símbolo — ao acertar, a área fica colorida, um marcador aparece e uma mensagem é exibida. A mensagem pode conter links externos que descrevem mais sobre iniciativas de coletivos e história dos marcos.
  - Possibilidade de liberar a rotação da cena após encontrar o símbolo, para explorar o entorno da região.

- **Mapa da Caminhada Volta Negra**
  - Visualização aérea baseada em **MapLibre GL JS** com tiles do **Carto Positron**.
  - Exibe o trajeto da caminhada como uma rota a pé baked (calculada pelo OSRM, perfil `foot`, usando Python).
  - Marcadores numerados em cada ponto de parada (Largo da Memória, Largo São Francisco, Largo da Misericórdia, Praça Antônio Prado) com pop-up descritivo.
  - Botão para alternar a visibilidade do trajeto (mostrar/ocultar).

## Estrutura do projeto

- `index.html` → lógica principal para cenas do Street View.  
- `scenes.json` → lista de cenas, cada uma com `id`, `title`, `embedSrc` e `hotspots`.  
- `map.html` → visualização do trajeto da caminhada em mapa interativo.  
- `routes.json` → definição das rotas, com lista de paradas e o caminho assado (`path.geometry.coordinates`).  
- `qrs/` → QR Codes para acesso rápido às cenas.  

## Como usar

1. Hospede o repositório em GitHub Pages (já disponível em: [cdviana.github.io/racism-game](https://cdviana.github.io/racism-game)).
2. Acesse diretamente cada cena via QR Code ou URL:
   - `...?s=NA` → abre a cena com ID `NA` definida no `scenes.json`.
   - `...?r=volta-negra-centro` → abre o mapa da caminhada no `map.html`.
3. Clique para tentar encontrar o símbolo.  
4. No caso do mapa, use o botão **Mostrar trajeto** para exibir a rota.

## Tecnologias

- [Google Maps Street View Embed API](https://developers.google.com/maps/documentation/embed/embedding-map)  
- [MapLibre GL JS](https://maplibre.org/maplibre-gl-js/)  
- Tiles Carto Positron (Carto + OpenStreetMap)  
- [OSRM](http://project-osrm.org/) para cálculo da rota a pé  

## 📜 Licença

Este projeto é de uso educacional e comunitário, sem fins lucrativos.
