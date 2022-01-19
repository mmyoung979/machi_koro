CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
    BEGIN NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update BEFORE
UPDATE
    ON games FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER trigger_update BEFORE
UPDATE
    ON players FOR EACH ROW EXECUTE PROCEDURE trigger_set_timestamp();
