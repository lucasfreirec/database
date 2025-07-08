#!/bin/bash

# Este script para a execução se qualquer comando falhar
set -e

# --- Configuração ---
API_URL="http://localhost:8000/api/v1"
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # Sem Cor

echo -e "${YELLOW}=====================================================${NC}"
echo -e "${YELLOW}  Iniciando Teste Completo da API da Clínica Vet   ${NC}"
echo -e "${YELLOW}=====================================================${NC}"

# --- Passo 1: Cadastrar Clínica ---
echo -e "\n${CYAN}--> Passo 1: Cadastrando uma nova Clínica (POST /clinicas)${NC}"
RESPONSE_CLINICA=$(curl -s -X POST "$API_URL/clinicas" \
     -H "Content-Type: application/json" \
     -d '{"nome": "Clínica Pata Amiga", "cidade": "Natal"}')
CLINICA_ID=$(echo "$RESPONSE_CLINICA" | jq -r '.id')
echo -e "${GREEN}SUCESSO: Clínica criada com ID: $CLINICA_ID${NC}"
echo "$RESPONSE_CLINICA" | jq .


# --- Passo 2: Cadastrar Veterinário ---
echo -e "\n${CYAN}--> Passo 2: Cadastrando uma Veterinária para a Clínica ID $CLINICA_ID (POST /veterinarios)${NC}"
RESPONSE_VET=$(curl -s -X POST "$API_URL/veterinarios" \
    -H "Content-Type: application/json" \
    -d '{"nome": "Dra. Ana Sousa", "especialidade": "Clínica Geral", "clinica_id": '$CLINICA_ID'}')
VET_ID=$(echo "$RESPONSE_VET" | jq -r '.id')
echo -e "${GREEN}SUCESSO: Veterinária criada com ID: $VET_ID${NC}"
echo "$RESPONSE_VET" | jq .


# --- Passo 3: Cadastrar Tutor ---
echo -e "\n${CYAN}--> Passo 3: Cadastrando um novo Tutor (POST /tutores)${NC}"
RESPONSE_TUTOR=$(curl -s -X POST "$API_URL/tutores" \
    -H "Content-Type: application/json" \
    -d '{"nome": "Carlos Mendes", "telefone": "84999998888"}')
TUTOR_ID=$(echo "$RESPONSE_TUTOR" | jq -r '.id')
echo -e "${GREEN}SUCESSO: Tutor criado com ID: $TUTOR_ID${NC}"
echo "$RESPONSE_TUTOR" | jq .


# --- Passo 4: Cadastrar Pet ---
echo -e "\n${CYAN}--> Passo 4: Cadastrando o pet 'Rex' para o Tutor ID $TUTOR_ID (POST /pets)${NC}"
RESPONSE_PET=$(curl -s -X POST "$API_URL/pets" \
    -H "Content-Type: application/json" \
    -d '{"nome": "Rex", "especie": "Cachorro", "idade": 5, "tutor_id": '$TUTOR_ID'}')
PET_ID=$(echo "$RESPONSE_PET" | jq -r '.id')
echo -e "${GREEN}SUCESSO: Pet criado com ID: $PET_ID${NC}"
echo "$RESPONSE_PET" | jq .


# --- Passo 5: Criar um Atendimento ---
echo -e "\n${CYAN}--> Passo 5: Criando um Atendimento para o pet $PET_ID com a vet $VET_ID (POST /atendimentos)${NC}"
RESPONSE_ATENDIMENTO=$(curl -s -X POST "$API_URL/atendimentos" \
    -H "Content-Type: application/json" \
    -d '{"descricao": "Check-up anual e vacinação.", "pet_id": '$PET_ID', "veterinario_id": '$VET_ID'}')
echo -e "${GREEN}SUCESSO: Atendimento criado com sucesso!${NC}"
echo "$RESPONSE_ATENDIMENTO" | jq .


# --- Passo 6: Verificações Finais ---
echo -e "\n${CYAN}--> Passo 6: Verificando os relacionamentos criados...${NC}"

echo -e "\n${YELLOW}Listando pets do Tutor ID $TUTOR_ID (GET /tutores/{id}/pets):${NC}"
curl -s -X GET "$API_URL/tutores/$TUTOR_ID/pets" | jq .

echo -e "\n${YELLOW}Listando todos os atendimentos (GET /atendimentos):${NC}"
curl -s -X GET "$API_URL/atendimentos" | jq .


echo -e "\n${GREEN}===========================================${NC}"
echo -e "${GREEN}  Teste de fluxo completo finalizado!    ${NC}"
echo -e "${GREEN}===========================================${NC}"