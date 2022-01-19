CREATE TABLE players (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    username TEXT,
    avatar INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE games (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    player1 INTEGER,
    player2 INTEGER,
    player3 INTEGER,
    player4 INTEGER,
    winner INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_winner FOREIGN KEY(winner) REFERENCES players(id)
);

CREATE TABLE player_coins_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER,
    player INTEGER,
    coins INTEGER,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id),
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id)
);

CREATE TABLE landmarks (
    id INTEGER,
    PRIMARY KEY(id),
    name TEXT,
    cost INTEGER
);

CREATE TABLE player_landmark_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER,
    player INTEGER,
    landmark INTEGER,
    activated BOOL DEFAULT False,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id),
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id),
    CONSTRAINT fk_landmark FOREIGN KEY(landmark) REFERENCES landmarks(id)
);

CREATE TABLE effect_turns (
    id INTEGER,
    PRIMARY KEY(id),
    name TEXT
);

CREATE TABLE industries (
    id INTEGER,
    PRIMARY KEY(id),
    name TEXT
);

CREATE TABLE buildings (
    id INTEGER,
    PRIMARY KEY(id),
    name TEXT,
    industry INTEGER,
    dice_roll INTEGER [],
    cost INTEGER,
    effect_turn INTEGER,
    CONSTRAINT fk_effect_turn FOREIGN KEY(effect_turn) REFERENCES effect_turns(id),
    CONSTRAINT fk_industry FOREIGN KEY(industry) REFERENCES industries(id)
);

CREATE TABLE player_building_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER,
    player INTEGER,
    building INTEGER,
    quantity INTEGER,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id) ON DELETE CASCADE,
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_building FOREIGN KEY(building) REFERENCES buildings(id) ON DELETE CASCADE
);
