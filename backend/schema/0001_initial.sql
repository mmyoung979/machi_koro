CREATE TABLE games (id AS IDENTITY)
CREATE TABLE players (name TEXT)
CREATE TABLE buildings (
    name TEXT,
    landmark BOOLEAN,
    type TEXT,
    dice_roll INT,
    cost INT,
)