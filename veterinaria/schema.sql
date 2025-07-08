DROP TABLE IF EXISTS atendimentos, pets, tutores, veterinarios, clinicas CASCADE;


CREATE TABLE clinicas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL
);


CREATE TABLE veterinarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    especialidade VARCHAR(255) NOT NULL,
    clinica_id INT NOT NULL,
    CONSTRAINT fk_clinica
        FOREIGN KEY(clinica_id) 
        REFERENCES clinicas(id)
        ON DELETE CASCADE
);


CREATE TABLE tutores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20)
);


CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    especie VARCHAR(100) NOT NULL,
    idade INT,
    tutor_id INT NOT NULL,
    CONSTRAINT fk_tutor
        FOREIGN KEY(tutor_id) 
        REFERENCES tutores(id)
        ON DELETE CASCADE
);


CREATE TABLE atendimentos (
    id SERIAL PRIMARY KEY,
    data TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    descricao TEXT NOT NULL,
    pet_id INT NOT NULL,
    veterinario_id INT NOT NULL,
    CONSTRAINT fk_pet
        FOREIGN KEY(pet_id) 
        REFERENCES pets(id),
    CONSTRAINT fk_veterinario
        FOREIGN KEY(veterinario_id) 
        REFERENCES veterinarios(id)
);

\echo '--------------------------------------'
\echo ' Tabelas criadas com sucesso!         '
\echo '--------------------------------------'