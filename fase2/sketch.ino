#include <DHT.h>

// Definição de Pinos
#define DHTPIN 4          // Pino do DHT22
#define DHTTYPE DHT22     // Tipo do sensor DHT
#define LDR_PIN 34        // Pino analógico para o LDR (pH)
#define BTN_N_PIN 23      // Botão Nitrogênio
#define BTN_P_PIN 22      // Botão Fósforo
#define BTN_K_PIN 21      // Botão Potássio
#define RELAY_PIN 5       // Pino do Relé Azul (Bomba d'água)

DHT dht(DHTPIN, DHTTYPE);

// Estados permanentes dos nutrientes (caso esteja usando a Opção 1 de interruptor/clique único)
bool nivelN = false;
bool nivelP = false;
bool nivelK = false;

// Variáveis para salvar a leitura anterior dos botões (debounce/clique único)
bool ultimoEstadoN = HIGH;
bool ultimoEstadoP = HIGH;
bool ultimoEstadoK = HIGH;

void setup() {
  Serial.begin(115200);
  
  dht.begin();
  pinMode(LDR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);
  
  pinMode(BTN_N_PIN, INPUT_PULLUP);
  pinMode(BTN_P_PIN, INPUT_PULLUP);
  pinMode(BTN_K_PIN, INPUT_PULLUP);
  
  digitalWrite(RELAY_PIN, LOW);
  
  Serial.println("=== Sistema de Irrigação Inteligente - Alface ===");
}

void loop() {
  // 1. Leitura da Umidade do Solo (DHT22)
  float umidadeSolo = dht.readHumidity();
  
  // 2. Leitura e Conversão do pH (LDR: 0-4095 mapeado para 0-14)
  int valorLDR = analogRead(LDR_PIN);
  float pH = map(valorLDR, 0, 4095, 14.0, 0.0);
  
  // 3. Leitura dos Botões NPK (Exemplo com alternância por clique único)
  bool leituraAtualN = digitalRead(BTN_N_PIN);
  if (leituraAtualN == LOW && ultimoEstadoN == HIGH) { nivelN = !nivelN; delay(50); }
  ultimoEstadoN = leituraAtualN;

  bool leituraAtualP = digitalRead(BTN_P_PIN);
  if (leituraAtualP == LOW && ultimoEstadoP == HIGH) { nivelP = !nivelP; delay(50); }
  ultimoEstadoP = leituraAtualP;

  bool leituraAtualK = digitalRead(BTN_K_PIN);
  if (leituraAtualK == LOW && ultimoEstadoK == HIGH) { nivelK = !nivelK; delay(50); }
  ultimoEstadoK = leituraAtualK;
  
  // Validação de erro de leitura do DHT
  if (isnan(umidadeSolo)) {
    Serial.println("Erro ao ler o sensor DHT22!");
    delay(2000);
    return;
  }
  
  // 4. Lógica de Decisão Inteligente Atualizada
  // Condições para irrigar:
  // - Umidade menor que 65%
  // - pH entre 5.5 e 7.5
  // - Pelo menos UM dos nutrientes (N, P ou K) deve ser True
  bool condicaoUmidade = (umidadeSolo < 65.0);
  bool condicaoPH = (pH >= 5.5 && pH <= 7.5);
  bool condicoesNutricionais = (nivelN || nivelP || nivelK); // Alterado para aceitar qualquer 1 nutriente
  
  bool ligarBomba = false;
  
  if (condicaoUmidade && condicaoPH && condicoesNutricionais) {
    digitalWrite(RELAY_PIN, HIGH); // Liga Relé Azul (Bomba)
    ligarBomba = true;
  } else {
    digitalWrite(RELAY_PIN, LOW);  // Desliga Relé Azul
    ligarBomba = false;
  }
  
  // 5. Exibição dos Dados no Monitor Serial
  Serial.println("----------------------------------------");
  Serial.print("Umidade do Solo: "); Serial.print(umidadeSolo); Serial.println("%");
  Serial.print("pH do Solo (LDR): "); Serial.println(pH, 1);
  Serial.print("Nitrogênio (N): "); Serial.println(nivelN ? "PRESENTE (True)" : "AUSENTE (False)");
  Serial.print("Fósforo (P): "); Serial.println(nivelP ? "PRESENTE (True)" : "AUSENTE (False)");
  Serial.print("Potássio (K): "); Serial.println(nivelK ? "PRESENTE (True)" : "AUSENTE (False)");
  Serial.print("Status da Bomba (Relé): "); 
  Serial.println(ligarBomba ? "LIGADA (Irrigando)" : "DESLIGADA");
  
  delay(3000);
}
