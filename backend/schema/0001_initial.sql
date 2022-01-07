CREATE TABLE games (timestamp TIMESTAMP);

CREATE TABLE players (username TEXT, avatar INTEGER);

CREATE TABLE buildings (
    name TEXT,
    landmark BOOLEAN,
    type TEXT,
    dice_roll INTEGER,
    cost INTEGER,
    effect_turn TEXT
);

INSERT INTO
    buildings (
        name,
        landmark,
        type,
        dice_roll,
        cost,
        effect_turn
    )
VALUES
    (
        'Wheat Field',
        False,
        'Agriculture',
        1,
        1,
        'Anyone'
    );
