CREATE TABLE players (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    avatar INTEGER,
    wins INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT unique_username UNIQUE(username),
    CONSTRAINT unique_email UNIQUE(email)
);

CREATE TABLE games (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    player1 INTEGER NOT NULL,
    player2 INTEGER NOT NULL,
    player3 INTEGER,
    player4 INTEGER,
    winner INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT fk_player1 FOREIGN KEY(player1) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_player2 FOREIGN KEY(player2) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_player3 FOREIGN KEY(player3) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_player4 FOREIGN KEY(player4) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_winner FOREIGN KEY(winner) REFERENCES players(id) ON DELETE CASCADE
);

CREATE TABLE player_coins_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER NOT NULL,
    player INTEGER NOT NULL,
    coins INTEGER NOT NULL,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id) ON DELETE CASCADE,
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id) ON DELETE CASCADE
);

CREATE TABLE landmarks (
    id INTEGER NOT NULL,
    PRIMARY KEY(id),
    name TEXT NOT NULL,
    cost INTEGER NOT NULL
);

CREATE TABLE player_landmark_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER NOT NULL,
    player INTEGER NOT NULL,
    landmark INTEGER NOT NULL,
    activated BOOL NOT NULL DEFAULT False,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id) ON DELETE CASCADE,
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_landmark FOREIGN KEY(landmark) REFERENCES landmarks(id) ON DELETE CASCADE
);

CREATE TABLE effect_turns (
    id INTEGER NOT NULL,
    PRIMARY KEY(id),
    name TEXT NULL
);

CREATE TABLE industries (
    id INTEGER NOT NULL,
    PRIMARY KEY(id),
    name TEXT NOT NULL
);

CREATE TABLE buildings (
    id INTEGER NOT NULL,
    PRIMARY KEY(id),
    name TEXT NOT NULL,
    industry INTEGER NOT NULL,
    dice_roll INTEGER [] NOT NULL,
    cost INTEGER NOT NULL,
    effect_turn INTEGER NOT NULL,
    CONSTRAINT fk_effect_turn FOREIGN KEY(effect_turn) REFERENCES effect_turns(id) ON DELETE CASCADE,
    CONSTRAINT fk_industry FOREIGN KEY(industry) REFERENCES industries(id) ON DELETE CASCADE
);

CREATE TABLE player_building_mapping (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY(id),
    game INTEGER NOT NULL,
    player INTEGER NOT NULL,
    building INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    CONSTRAINT fk_game FOREIGN KEY(game) REFERENCES games(id) ON DELETE CASCADE,
    CONSTRAINT fk_player FOREIGN KEY(player) REFERENCES players(id) ON DELETE CASCADE,
    CONSTRAINT fk_building FOREIGN KEY(building) REFERENCES buildings(id) ON DELETE CASCADE
);
